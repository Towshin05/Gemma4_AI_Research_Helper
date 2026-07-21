# 📚 AI Research Gap 

An AI-powered research assistant that processes multiple research papers and builds a semantic knowledge base for Retrieval-Augmented Generation (RAG).

The project extracts text from PDFs, detects paper sections, splits documents into semantic chunks, generates embeddings, and stores them in a vector database for intelligent retrieval.

---

## 🚀 Features Implemented

- Upload up to 5 research papers (PDF)
- Automatic PDF text extraction
- Research paper section detection
- Semantic text chunking
- Sentence embedding generation
- ChromaDB vector database integration
- Persistent vector storage
- Metadata storage for each chunk
- Interactive Streamlit interface
- Document statistics visualization

---

## 🛠 Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- LangChain Text Splitters

---

## 📂 Current Pipeline

```text
Upload PDF(s)
      ↓
Extract Text
      ↓
Detect Paper Sections
      ↓
Split into Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
```

---

## 📁 Project Structure

```
ResearchGapAI/
│
├── app.py
├── config.py
├── modules/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── context_extractor.py
│   ├── embedding_generator.py
│   └── chroma_manager.py
│
├── data/
│   └── uploaded_papers/
│
├── vector_db/
│
└── README.md
```

---

## 📦 Modules Completed

### ✅ PDF Loader
- Extracts text from uploaded research papers.

### ✅ Context Extractor
Detects common research paper sections including:
- Abstract
- Introduction
- Methodology
- Results
- Discussion
- Limitations
- Future Work
- Conclusion
- References

### ✅ Text Splitter
Splits long research papers into overlapping semantic chunks suitable for embedding.

### ✅ Embedding Generator
Generates dense vector embeddings using Sentence Transformers.

### ✅ ChromaDB Manager
Stores:
- Chunk text
- Embeddings
- Metadata
- Unique IDs

using a persistent vector database.

---

## 🔄 Current Development Stage

The indexing pipeline has been completed.

Next milestone:

- Semantic Retrieval
- Question Embedding
- Similarity Search
- Retrieval-Augmented Generation (Gemma 4)
- Research Gap Detection
- Cross-paper Comparison
- Future Work Recommendation

---

## 🎯 Goal

Build an AI research assistant capable of:

- Answering questions across multiple research papers
- Identifying research gaps
- Comparing methodologies
- Extracting limitations
- Suggesting future research directions
- Providing citation-aware responses

---

##  Author

**Towshin Hossain**

CUET — Computer Science & Engineering