import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="Rental Project Chatbot", layout="centered")

st.title("🏠 Rental Management System Chatbot")
st.write("Ask anything about Rental-Management-System project ")

# Load PDF
loader = PyPDFLoader("RentalHub.pdf")
documents = loader.load()

# Split PDF text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
texts = text_splitter.split_documents(documents)

# FREE embeddings (no API key)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector database
db = FAISS.from_documents(texts, embeddings)

# Search bar
query = st.text_input("🔍 Enter your question")

# Button
if st.button("Search"):
    if query:
        docs = db.similarity_search(query, k=3)
        st.subheader("🤖 Answer")
        for doc in docs:
            st.write(doc.page_content)
    else:
        st.warning("Please enter a question")
