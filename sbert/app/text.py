from transformers import TFBertModel, AutoTokenizer
import tensorflow as tf
import tensorflow_addons as tfa
import os 


tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def convert_example_to_feature(text):
    return tokenizer(text = text, return_tensors = 'tf',
                            padding='max_length',
                            max_length = 128, 
                            add_special_tokens = True)
    
  # map to the expected input to TFBertForSequenceClassification
def map_example_to_dict(input_ids, attention_masks, token_type_ids):
    return {
      "input_ids": tf.squeeze(input_ids, 0),
      "token_type_ids": tf.squeeze(token_type_ids, 0),
      "attention_mask": tf.squeeze(attention_masks, 0),
    }

def encode_examples(ds):
    # prepare list, so that we can build up final TensorFlow dataset from slices.
    input_ids_list = []
    token_type_ids_list = []
    attention_mask_list = []
    for review in ds:
        bert_input = convert_example_to_feature(review)
        input_ids_list.append(bert_input['input_ids'])
        token_type_ids_list.append(bert_input['token_type_ids'])
        attention_mask_list.append(bert_input['attention_mask'])


    return tf.data.Dataset.from_tensor_slices((input_ids_list, attention_mask_list, token_type_ids_list)).map(map_example_to_dict)


# @tf.keras.utils.register_keras_serializable()
class Pooling(tf.keras.layers.Layer):
  def __init__(self, **kwargs):
    super(Pooling, self).__init__(**kwargs)

  def get_config(self):
        config = super(Pooling, self).get_config()
        return config

  def call(self, model_output, attention_mask):
    token_embeddings = model_output["last_hidden_state"] #First element of model_output contains all token embeddings
    input_mask_expanded = tf.cast(tf.tile(tf.expand_dims(attention_mask, axis =-1), [1,1, token_embeddings.shape[-1]]), tf.float32)
    sum_embeddings = tf.math.reduce_sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = tf.clip_by_value(tf.math.reduce_sum(input_mask_expanded, axis =1), clip_value_min= 1e-9, clip_value_max=10000)
    return sum_embeddings / sum_mask




def import_model():
    #importing the model
    print(os.getcwd())
    model_path = "/code/app/app/SentenceBertModel.h5"
    return tf.keras.models.load_model(model_path, custom_objects = 
    {"Pooling": Pooling, "TFBertModel": TFBertModel,
     "Addons>MultiOptimizer": tfa.optimizers.MultiOptimizer})



