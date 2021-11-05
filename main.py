import os
import random
import re
import numpy as np
import tensorflow as tf
from tensorflow.keras import models

# length of song to be generated
SONGLEN = 1000

# loading the saved model
model = models.load_model('model_100')

def sample(preds):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# load the data to generate a starting string
path = 'data'
data = ''
files = ['bieber', 'bruno-mars', 'drake', 'rihanna', 'adele']
for file in files:
    if os.path.isfile(os.path.join(path, file + '.txt')):
        file_content = open(os.path.join(path, file + '.txt'), 'r', encoding='utf-8').read()
        data += file_content

# Replace all non ascii characters in data with ''
data = re.sub(r'[^\x00-\x7F]', r'', data)

# creating conversion dictionaries
chars = sorted(set(data))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# select a random start string
maxlen = 40
start_index = random.randint(0, len(data) - maxlen - 1)
sentence = data[start_index : start_index + maxlen]

generated = sentence
for i in range(SONGLEN):
    x_pred = np.zeros((1, maxlen, len(chars)))
    for t, char in enumerate(sentence):
        x_pred[0, t, char_indices[char]] = 1.0
        
    preds = model.predict(x_pred)[0]

    next_index = sample(preds)
    next_char = indices_char[next_index]
    sentence = sentence[1:] + next_char
    generated += next_char

print('\n\n')
print(generated)