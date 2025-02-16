# Creating API for chatbot which use Paid LLMs

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI  # this have paid llm models 

from langserve import add_routes
import uvicorn



# Import the Ollama class instead of the module
from langchain_community.llms.ollama import Ollama


import streamlit as st
# os helps to get value which present inside environment value 
# import os
from dotenv import load_dotenv  # helps to load env files


# laod all env variables 
load_dotenv()

# This use if an only if we are using paid llm model
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple Api Server"
)

print("app : ", app)


# add_routes(
#     app, 
#     ChatOpenAI(),
#     path="/openai"
# )

# Open Ai LLm model
# model = ChatOpenAI()

# Ollama llm model
llm = Ollama(model="llama2")

# prompt1 = ChatPromptTemplate.from_template("Write an esssay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 1000 words")

# add_routes(
#     app,
#     prompt1 |model,
#     path="/essay"
# )


add_routes(
    app,
    prompt2 |llm,
    path="/poem"
)


if __name__ == "__main__":
    uvicorn.run(app , host="localhost", port=8000)
