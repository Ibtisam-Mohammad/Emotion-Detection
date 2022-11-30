import pickle
with open('result.pickle','rb') as f:
    dir_=pickle.load(f)
print(dir_)