# FinalSubmissionAI5

Hello everyone,

This repository contains the EDAA app. EDAA stands for Emotion Detection and Analysis. It is a web application which will create a report of audience reactions. We take into consideration, video (facial expressions of the audience) and text (context of the speech) data. This app will help public speakers improve their speech. Please read more about our app in the about section of our [web app](http://34.102.62.14/about). 

The following is a diagram of the architecture of our web app:
![img](https://github.com/aamir09/FinalSubmissionAI5/blob/main/webapp_architecture.PNG "webapp_architecture.PNG")

As you can see from the plot above,
The user will input a video into the web app. The ![Upload](https://github.com/aamir09/FinalSubmissionAI5/blob/main/frontend_react/src/components/Upload.js) component of the frontend-react downloads the video to the server after encoding it.
This video is then taken by the ![preprocessor](https://github.com/aamir09/FinalSubmissionAI5/tree/main/preprocessor) which first decodes it. 
Once decoded audio is extracted from the video using moviepy.
Then it is divided into chunks by using the preprocessor. The preprocessor divides the audio into 10 second chunks.
These audio chunks are the converted to text using the ![ASR container](https://github.com/aamir09/FinalSubmissionAI5/tree/main/OpenAI-ASR).
These sentences are analysed using ![SBert](https://github.com/aamir09/FinalSubmissionAI5/tree/main/sbert).
The sbert container predicts the sentiment of the model and saves the audio predictions to the GCS bucket.
Here is a screenshot of the bucket to get a basic idea of the structure.
![img](https://github.com/aamir09/FinalSubmissionAI5/blob/main/GCS_bucket.jpeg)
The results look something like this :
{
  "0_10": {
    "sentence": "I'm goin",
    "prediction": "negative",
    "start": 0,
    "stop": 10
  },
  "10_20": {
    "sentence": "to go to the museum",
    "prediction": "neutral",
    "start": 10,
    "stop": 20
  },
  "20_30": {
    "sentence": "Good Bye",
    "prediction": "neutral",
    "start": 20,
    "stop": 30
  },
  "30_40": {
    "sentence": "Thank",
    "prediction": "positive",
    "start": 30,
    "stop": 40
  },
}
The key of the dictionary specify the start and the stop time, i.e. the interval. the value is a dictionay which has the the following information :
- sentence - this has been predicted by the asr model when the input audio chunk is given as input.
- prediction - this has been predicted by the sentence bert model when the sentence is given as input.
- start - start time
- stop - stop time

