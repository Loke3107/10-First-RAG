# First RAG App

https://loke-first-rag.streamlit.app/

A simple Retrieval-Augmented Generation (RAG) application built with Streamlit, ChromaDB, and OpenRouter.

## Features

* Ask questions in natural language
* Retrieves relevant documents using ChromaDB
* Generates answers using an LLM
* Displays retrieved documents for transparency
* Prevents hallucinations by answering only from the provided context

## Tech Stack

* Python
* Streamlit
* ChromaDB
* OpenRouter
* DeepSeek Chat Model

## How It Works

User Question
↓
Retrieve Relevant Documents
↓
Build Context
↓
LLM Generates Answer
↓
Display Response


## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```
