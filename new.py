from fastapi import FastAPI
from langchain.llms import Ollama

# Initialize the model using LangChain and Ollama
llm = Ollama(model="biomistral1")  # Use the correct model name you pulled locally

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the medical query API"}

@app.get("/predict")
def predict(query: str):
    # Run the query through the LangChain model
    response = llm(query)
    return {"response": response}

