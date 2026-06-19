import streamlit as st
import chromadb
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
    )

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="knowledge_base"       )

documents=[
        "Python is a programming language",
        "Java is used for enterprise applications",
        "Machine Learning is a subset of AI",
        "Deep Learning uses neural networks",
        "Banana is a fruit",
        "Brinjal is a vegetable",
        "Car is a vehicle",
        "Truck is a heavy vehicle",
        "AI is hard to learn"
    ]

try:
    collection.add(
        documents= documents,
        ids=[str(i) for i in range(len(documents))]
    )
except:
    pass

st.title("First RAG App")
with st.expander("View the collections"):
    for doc in documents:
        st.write(f"- {doc}")

query = st.text_input(
    "Ask a question: "
)

if st.button("Ask"):
    if not query.strip():
        st.warning("Enter a question: ")
        st.stop()
    results = collection.query(
        query_texts = [query],
        n_results=3
    )

    retrieved_docs = results["documents"][0]

    with st.expander("View the retrieved documents"):
        for i, doc in enumerate(retrieved_docs):
            st.write(f"{i+1}. {doc}")

    #Build context for LLM

    context = "\n".join(retrieved_docs)
    

    prompt = f"""
    you are a helpful assistant. Use the following context to answer the question. If the answer is not in the context, say "I don't know" based on 
    the provided context.

Context:
{context}
Question: {query}
"""
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    answer = response.choices[0].message.content
    st.subheader("Answer:")
    st.write(answer)