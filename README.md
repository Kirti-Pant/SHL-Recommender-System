# 🧠 SHL GenAI Assessment Recommendation System

An AI-powered system that recommends SHL assessments based on natural language job descriptions or hiring needs. It uses generative AI and semantic search to identify the most relevant tests from SHL’s assessment catalog.

---

## 🚀 Live Demos

- **🔗 Streamlit App**: [https://your-streamlit-app.streamlit.app](#)
- **🔗 FastAPI Endpoint**: [https://shl-fastapi-efc6.onrender.com/recommend](https://shl-fastapi-efc6.onrender.com/recommend)
- **📄 Swagger UI**: [https://shl-fastapi-efc6.onrender.com/docs](https://shl-fastapi-efc6.onrender.com/docs)

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **NLP/AI**: Sentence-Transformers, Gemini (Google Generative AI)
- **Vector Search**: FAISS
- **Other**: Huggingface Hub, Requests, Pydantic

---

## 📦 Features

- Input free-text queries like job descriptions or candidate requirements
- Automatically enhances queries using Gemini
- Retrieves semantically relevant SHL assessments using vector search
- Returns test name, type, duration, and remote/adaptive support info

---

## 🔁 Pipeline Overview

1. **User Query**: A job description or skill requirement is entered.
2. **Query Enhancement**: Gemini improves and refines the input.
3. **Embedding**: Enhanced query is embedded using `sentence-transformers`.
4. **Similarity Search**: FAISS retrieves top matching SHL assessments from a vector index.
5. **Response**: Returns JSON list of recommended assessments with metadata.

---

## 🧪 Sample Input & Output

### Input:
```json
{
  "query": "Looking to assess Python skills, logical reasoning, and communication"
}
