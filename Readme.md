# 📚 AI Research Helper

An AI-powered Research Assistant built using **Gemma 4**, **ChromaDB**, **Sentence Transformers**, and **Streamlit**.

The system helps students and researchers understand research papers, compare multiple papers, identify research gaps, explain methodologies, review papers, and answer research questions using Retrieval-Augmented Generation (RAG).

---

# Features

## PDF Processing

- Upload up to 5 research papers
- Automatic PDF text extraction
- Section detection
- Semantic text chunking

---

## Semantic Search

- Sentence Transformer embeddings
- ChromaDB vector database
- Similarity search
- Retrieval-Augmented Generation (RAG)

---

## AI Reasoning using Gemma 4

The project uses

```
google/gemma-4-26b-a4b-it:free
```

through **OpenRouter API**.

Gemma is responsible for

- Research Question Answering
- Paper Summarization
- Paper Comparison
- Methodology Explanation
- Research Gap Detection
- Future Work Suggestions
- Reviewer Mode
- Full Paper Reasoning

---

## Supported Research Tasks

- Summarize paper
- Compare papers
- Explain methodology
- Extract limitations
- Detect research gaps
- Suggest future work
- Review research paper
- Answer research questions

---

# Project Structure

```
AIResearchHelper/
│
├── app.py
├── config.py
├── ui.py
│
├── data/
│
├── modules/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── context_extractor.py
│   ├── embedding_generator.py
│   ├── chroma_manager.py
│   ├── prompt_builder.py
│   ├── intent_detector.py
│   ├── response_formatter.py
│   ├── reasoning_engine.py
│   └── gemma_client.py
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- OpenRouter API
- Gemma 4
- PyPDF
- HuggingFace Embeddings

---

# Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AIResearchHelper.git

cd AIResearchHelper
```

---

# Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run Streamlit

```bash
streamlit run app.py
```

---

# Open in Browser

```
http://localhost:8501
```

---

# Gemma 4 Setup

The project uses

```
google/gemma-4-26b-a4b-it:free
```

through OpenRouter.

---

## Step 1

Create an account

https://openrouter.ai

---

## Step 2

Generate an API Key

Dashboard

↓

API Keys

↓

Create Key

---

## Step 3

Create a `.env`

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## Step 4

Gemma Client

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
```

---

## Model Used

```python
google/gemma-4-26b-a4b-it:free
```

---

## Generate Response

```python
response = client.chat.completions.create(
    model="google/gemma-4-26b-a4b-it:free",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)
```

---

# RAG Pipeline

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
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
Embedding
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
Answer
```

---

# Intent Detection

The system automatically detects the user intent.

Supported intents

- summary
- comparison
- methodology
- reviewer
- research_gap
- future_work
- limitations
- general

---

# Full Paper Reasoning

Some questions require the complete paper instead of only retrieved chunks.

Example

- Compare all uploaded papers
- Find research gaps
- Review the paper
- Explain overall methodology

For these queries the entire extracted papers are passed to Gemma.

---

# Semantic Search

Normal questions use RAG.

Workflow

```
Question

↓

Embedding

↓

Top Similar Chunks

↓

Gemma

↓

Answer
```

---

# Chat Features

- Chat history
- Multi-turn conversation
- User and AI avatars
- Persistent session

---

# Future Improvements

- Image understanding
- Research roadmap generator
- Related paper recommendation
- Citation generation
- Research mentor mode
- Experiment planning
- Figure explanation
- Dataset recommendation

---

# Commands Used During Development

Clone

```bash
git clone REPOSITORY_URL
```

Create venv

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

Freeze packages

```bash
pip freeze > requirements.txt
```

Git status

```bash
git status
```

Add files

```bash
git add .
```

Commit

```bash
git commit -m "Initial Commit"
```

Push

```bash
git push origin main
```

---

# Author

Towshin Hossain

Department of Computer Science and Engineering

Chittagong University of Engineering & Technology (CUET)

Bangladesh

---

# License

MIT License