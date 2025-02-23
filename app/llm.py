from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import text2emotion
import nltk
import warnings
import os
import sys
import numpy as np


# Suppress warnings and unnecessary logs
warnings.filterwarnings("ignore")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# Suppress NLTK download messages
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

nltk.download('punkt')

# Load model and tokenizer
model_name = "microsoft/DialoGPT-medium"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name, output_hidden_states=True)
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

#Better ai but very expensive space-speed-wise
#mname = "facebook/blenderbot-400M-distill"

def get_embedding(query):
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model(**inputs)
    hidden_states = outputs.hidden_states
    last_hidden_state = hidden_states[-1]
    query_embedding = last_hidden_state.mean(dim=1)
    return query_embedding

def chat(prompt):
    input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

def get_emotions(prompt: str):
    emotions = text2emotion.get_emotion(prompt)
    expected_keys = ["Happy", "Angry", "Surprise", "Sad", "Fear"]
    tmp = [emotions.get(key, 0) for key in expected_keys]
    emotions_array = np.array(tmp, dtype=np.float32)
    return emotions_array


# Get user input and process it
"""
while(1):
    query = input("You: ")
    response = chat(query)
    query_embedding = get_embedding(query)
    emotions = text2emotion.get_emotion(query)

    print("\nEmbedding Tensor:", query_embedding)
    print("Embedding Shape:", query_embedding.shape)
    print("Chatbot Response:", response)
    print("Emotions:", emotions)
    print("Emotion Values:", list(emotions.values()))"""

