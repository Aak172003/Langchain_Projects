import streamlit as st
import requests

import os

from dotenv import load_dotenv  # helps to load env files


load_dotenv()

print("os.getenv('LANGCHAIN_API_KEY') ::::::: ", os.getenv('LANGCHAIN_API_KEY'))
# call langsmith for tracking 
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"



def get_openai_response(input_text):

    print("input_text :::::::::::: ", input_text)
    # as for now i don't have a paid llm so i am  calling open-source llm api 
    response = requests.post("http://localhost:8000/poem/invoke", json={'input':{'topic':input_text}})
    print("response.json()['output'] for paid  :::::::::::::::::::::::: ", response.json()['output'])
    return response.json()['output']


# Opensource llm model
def get_ollama_response(input_text1):
    response = requests.post("http://localhost:8000/poem/invoke", json={'input':{'topic':input_text1}})
    print("response.json()['output'] for open-source :::::::::::::: ", response.json()['output'])
    return response.json()['output']


st.title("Langchain demo with openai llama2 api chains ")

input_text = st.text_input("Write an essay on ")
input_text1 = st.text_input("Write an poem on ")



if input_text:
    st.write(get_openai_response(input_text))


if input_text1:
    st.write(get_ollama_response(input_text1))