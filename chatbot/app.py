# First have to import these 3 libraries 

# This contains paid llm models 
# from langchain_openai import ChatOpenAI  # this have paid llm models 

from langchain_core.prompts import ChatPromptTemplate   # use to create custom prompts
from langchain_core.output_parsers import StrOutputParser   # helps to manage type of string and how it will gonna show 


# Import the Ollama class instead of the module
from langchain_community.llms.ollama import Ollama

import streamlit as st
# os helps to get value which present inside environment value 
import os
from dotenv import load_dotenv  # helps to load env files

load_dotenv()

# environment variables calls 
# This will only use in case of paid llms 
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# call langsmith for tracking 
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Now start creating chatbot 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please provide response to user queries"), 
    ("user", "Question:{question}")
])

# Streamlit framework
st.title("Langchain Demo Project with LLama 2")
input_text = st.text_input("Search the topic you want")

# Use the Ollama LLM call with the correct class
llm = Ollama(model="llama2")

output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
