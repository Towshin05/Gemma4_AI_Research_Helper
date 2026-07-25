# 📚 AI Research Helper

### AI-Powered Research Assistant using **Gemma 4**, **Retrieval-Augmented Generation (RAG)**, **ChromaDB**, and **Sentence Transformers**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemma4](https://img.shields.io/badge/Gemma-4-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Project Overview

AI Research Helper is an intelligent research paper review assistant designed to help students, researchers, and academics analyze scientific papers more efficiently.

Instead of manually reading hundreds of pages, users can upload multiple research papers and interact with them using natural language.

The application combines **Retrieval-Augmented Generation (RAG)** with **Google Gemma 4** to provide context-aware answers, summarize papers, compare methodologies, identify research gaps, review papers, and generate research recommendations.

The goal is to significantly reduce the time required for literature review while improving research productivity.

---

# 🎯 Problem Statement

Researchers often spend days or even weeks reading numerous papers before they can:

- Understand a research topic
- Compare existing methods
- Identify research gaps
- Analyze limitations
- Find future research opportunities

Traditional PDF readers provide only document viewing capabilities and do not support intelligent reasoning across multiple papers.

AI Research Helper addresses this challenge by enabling researchers to upload multiple papers and interact with them through natural language questions powered by **Gemma 4**.

---

# 🤖 Why Gemma 4?

Gemma 4 serves as the reasoning engine of the application.

Unlike traditional retrieval systems that simply return relevant text chunks, Gemma 4 understands scientific context and produces research-level responses.

Gemma 4 is responsible for:

- Multi-paper reasoning
- Research paper summarization
- Methodology comparison
- Research gap detection
- Future work generation
- Reviewer mode
- Research advisor recommendations
- Multi-turn conversations
- Context-aware scientific question answering

Without Gemma 4, the system would only retrieve document chunks instead of generating meaningful research insights.

---



# ✨ Key Features

## 📄 PDF Processing

- Upload up to **5 research papers**
- Automatic PDF text extraction
- Section detection
- Intelligent semantic chunking

---

## 🔍 Retrieval-Augmented Generation (RAG)

- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic similarity search
- Context-aware retrieval
- Intelligent prompt construction

---

## 🧠 AI-Powered Research Assistant

Powered by **Gemma 4** through OpenRouter.

Supports:

- Research Question Answering
- Literature Review
- Multi-paper Comparison
- Methodology Analysis
- Research Gap Detection
- Future Work Suggestions
- Reviewer Mode
- Research Advisor Mode
- Full Paper Reasoning

---

## 💬 Conversational AI

- Multi-turn conversations
- Chat history
- Context-aware follow-up questions
- Recent question history
- Interactive Streamlit interface

---

# 📂 Project Structure

```text
Gemma4_AI_Research_Helper/
│
├── app.py                     # Main Streamlit application
├── config.py                  # Configuration settings
├── ui.py                      # User Interface
│
├── data/                      # Uploaded research papers
│
├── modules/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── context_extractor.py
│   ├── embedding_generator.py
│   ├── chroma_manager.py
│   ├── prompt_builder.py
│   ├── intent_detector.py
│   ├── reasoning_engine.py
│   ├── response_formatter.py
│   └── gemma_client.py
│
├── chroma_db/                 # Vector database
├── requirements.txt
├── README.md
└── .env
```

---

# 🏗️ System Architecture

The application follows a modular Retrieval-Augmented Generation (RAG) architecture.

```text
                   User
                     │
                     ▼
           Upload Research Papers
                     │
                     ▼
              PDF Text Extraction
                     │
                     ▼
              Semantic Chunking
                     │
                     ▼
          Sentence Transformer
              Embedding Model
                     │
                     ▼
                 ChromaDB
             Vector Database
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
  Similarity Search        Full Paper Retrieval
        │                         │
        └────────────┬────────────┘
                     ▼
              Prompt Builder
                     │
                     ▼
                Gemma 4 LLM
                     │
                     ▼
          Response Formatter
                     │
                     ▼
                 Final Answer
```

---

# 🔄 RAG Pipeline

The application follows the Retrieval-Augmented Generation (RAG) workflow shown below.

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Semantic Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Intent Detection
      │
      ▼
Similarity Search
      │
      ▼
Prompt Builder
      │
      ▼
Gemma 4
      │
      ▼
AI Response
```

---

# 🧠 Intelligent Reasoning

The application dynamically chooses between two reasoning strategies.

### 🔹 Retrieval-Augmented Generation (RAG)

For general research questions:

- Similarity Search
- Top-k document retrieval
- Context-aware prompting
- Fast responses

Example:

- Explain this methodology
- Summarize this section
- What dataset was used?

---

### 🔹 Full Paper Reasoning

For complex analytical tasks, the system bypasses retrieval and provides the complete extracted papers to Gemma 4.

This enables:

- Multi-paper comparison
- Literature review
- Research gap identification
- Reviewer mode
- Research advisor mode

This hybrid reasoning strategy improves both efficiency and reasoning quality.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| Streamlit | Interactive Web Interface |
| Gemma 4 | Large Language Model |
| OpenRouter API | Gemma 4 API Access |
| ChromaDB | Vector Database |
| Sentence Transformers | Embedding Generation |
| PyMuPDF | PDF Text Extraction |
| Hugging Face | Embedding Models |
| NumPy | Numerical Operations |
| Regular Expressions | Section Detection |

---



# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Towshin05/Gemma4_AI_Research_Helper.git

cd Gemma4_AI_Research_Helper
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Gemma 4

The application uses

```
google/gemma-4-26b-a4b-it:free
```

through **OpenRouter API**.

---

## Step 1

Create an OpenRouter account:

https://openrouter.ai

---

## Step 2

Generate an API Key.

Dashboard

↓

API Keys

↓

Create Key

---

## Step 3

Create a `.env` file in the project root.

```text
OPENROUTER_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file to GitHub. It should be listed in `.gitignore`.

---

#  Run the Application

```bash
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

# 🎯 Example Questions

Users can ask questions naturally, such as:

- Compare these research papers.
- Summarize this paper.
- Explain the proposed methodology.
- Identify the research gaps.
- What are the limitations?
- Suggest future work.
- Which paper should I follow?
- Compare the datasets used.
- Review this paper like a NeurIPS reviewer.
- Recommend a research direction based on these papers.

---

# ⚠️ Current Limitations

- Supports PDF documents only.
- OCR for scanned PDFs is not yet supported.
- Maximum of five uploaded papers.
- Citation generation is not yet available.

---

#  Future Roadmap

Planned improvements include:

- 📄 Automatic literature review generation
- 📚 Citation generation
- 🖼 Figure and table understanding
- 🧪 Experiment planning assistant
- 🔍 Related paper recommendation
- 📝 Research proposal generation
- 🌍 Multi-language support
- ☁️ Cloud deployment
- 📑 PDF annotation and highlighting

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas for improvements or discover bugs:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 👨‍💻 Author

**Towshin Hossain**

Department of Computer Science and Engineering

Chittagong University of Engineering & Technology (CUET)

Bangladesh

GitHub:

https://github.com/Towshin05

---

# Contributor

**Arupa Barua**
Department of Computer Science and Engineering

Chittagong University of Engineering & Technology (CUET)

Bangladesh
---
# 📄 License

This project is licensed under the **MIT License**.

---

#  Acknowledgements

This project was developed using:

- Google Gemma 4
- OpenRouter API
- Streamlit
- ChromaDB
- Sentence Transformers
- Hugging Face
- PyMuPDF

Special thanks to the **Google Gemma 4 Hackathon** for providing the opportunity to build this project.