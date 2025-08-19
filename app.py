import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

## Model Loading 
model = load_model("next_word_GRU_lstm.h5")

## Loading the Tokenizer
with open("tokenizer.pickle","rb") as handle:
    tokenizer = pickle.load(handle)


## Function to predict the next word
def predict_word(model,tokenizer, text, max_sequence_len):
  token_list = tokenizer.texts_to_sequences([text])[0]
  if len(token_list) >= max_sequence_len:
    token_list = token_list[-(max_sequence_len-1):] ## Ensuring the sequence length matches max_sequence_len
  token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
  prediction = model.predict(token_list, verbose=0)
  predicted_word_index = np.argmax(prediction, axis=1)
  for word, index in tokenizer.word_index.items():
    if index == predicted_word_index:
      return word
  return None



## Streamlit App
import streamlit as st

st.title("Next Word Prediction Uisng LSTM")

input_text = st.text_input("Enter the sequence of Words")
if st.button("Predict the Next Word"):
  max_sequence_len = model.input_shape[1]+1 # Retrieving the max sequence length from the model
  next_word = predict_word(model,tokenizer, input_text, max_sequence_len )
  st.write(f"MODEL PREDICTION")
  st.write(f"Next Word:  {next_word}")

