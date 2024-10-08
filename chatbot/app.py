from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# OPEN AI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# LangChain API Key
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Initialize the streamlit framework
st.title("Langchain demo with OpenAI")
input_text = st.text_input("Search for a topic")

# Define the Open AI model
open_ai_llm = ChatOpenAI(model="gpt-3.5-turbo")

# Define the output parser
output_parser = StrOutputParser()

# Define the chain
chain = prompt | open_ai_llm | output_parser

# Write the response
if input_text:
    st.write(chain.invoke({"question":input_text}))

