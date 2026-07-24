import streamlit as st

from config import UPLOAD_DIR
from ui import UI

from modules.pdf_loader import PDFLoader
from modules.text_splitter import PDFTextSplitter
from modules.context_extractor import ContextExtractor
from modules.embedding_generator import EmbeddingGenerator
from modules.prompt_builder import PromptBuilder
from modules.chroma_manager import ChromaManager
from modules.intent_detector import IntentDetector
from modules.response_formatter import ResponseFormatter
from modules.reasoning_engine import ReasoningEngine
from modules.gemma_client import GemmaClient

# -----------------------------------------
# Streamlit Config
# -----------------------------------------
st.set_page_config(
    page_title="AI Research Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

DEBUG = False

# -----------------------------------------
# Session State
# -----------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "papers" not in st.session_state:
    st.session_state.papers = {}

# -----------------------------------------
# Initialize Modules
# -----------------------------------------

loader = PDFLoader()
splitter = PDFTextSplitter()
context = ContextExtractor()
embedder = EmbeddingGenerator()
db = ChromaManager()
prompt_builder = PromptBuilder()
detector = IntentDetector()
formatter = ResponseFormatter()
reasoner = ReasoningEngine()
gemma = GemmaClient()
ui = UI()

# -----------------------------------------
# UI
# -----------------------------------------

ui.load_css()
ui.show_header()

uploaded_files = st.file_uploader(
    "Upload your research papers",
    type=["pdf"],
    accept_multiple_files=True,
    help="Upload up to 5 research papers."
)

if uploaded_files and len(uploaded_files) > 5:
    st.error("Maximum 5 PDFs allowed.")
    st.stop()



    
ui.show_sidebar(uploaded_files,db)
                
                
                
                
# -----------------------------------------
# Process Uploaded PDFs
# -----------------------------------------

if uploaded_files:

    for pdf in uploaded_files:

        # Skip if already processed
        if pdf.name in st.session_state.papers:
            continue

        save_path = UPLOAD_DIR / pdf.name

        with open(save_path, "wb") as f:
            f.write(pdf.getbuffer())

        text = loader.extract_text(save_path)

        st.session_state.papers[pdf.name] = text

        chunks = splitter.split_text(text)

        embeddings = embedder.generate_embeddings(chunks)

        db.add_documents(
            chunks=chunks,
            embeddings=embeddings,
            paper_name=pdf.name
        )

# -----------------------------------------
# Chat Section
# -----------------------------------------

st.divider()
st.header("💬 Ask Questions")

if not st.session_state.papers:
    st.warning("Upload at least one research paper to start chatting.")
    st.stop()
# Display previous conversation

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# -----------------------------------------
# User Input
# -----------------------------------------

user_query = st.chat_input(
    "Ask anything about your uploaded papers..."
)

if user_query:

    # show user instantly
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_query)

    intent = detector.detect_intent(user_query)



    # =====================================
    # FULL PAPER REASONING
    # =====================================

    if reasoner.requires_full_papers(intent):

        documents = list(st.session_state.papers.values())

        metadatas = [
            {
                "paper_name": name
            }
            for name in st.session_state.papers.keys()
        ]

        prompt = prompt_builder.build_prompt(
            intent=intent,
            question=user_query,
            documents=documents,
            metadatas=metadatas,
            messages=st.session_state.messages
        )

    # =====================================
    # NORMAL RAG
    # =====================================

    else:

        query_embedding = embedder.generate_embeddings(
            [user_query]
        )

        results = db.search(query_embedding)
        
        if not results["documents"] or not results["documents"][0]:
            st.error("No relevant content found in the uploaded papers.")
            st.stop()

        prompt = prompt_builder.build_prompt(
            intent=intent,
            question=user_query,
            documents=results["documents"][0],
            metadatas=results["metadatas"][0],
            messages=st.session_state.messages
        )

    # =====================================
    # Gemma
    # =====================================

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Gemma is analyzing the papers..."):
            try:
                

                answer = gemma.generate_response(prompt)

                if not answer:
                    answer = "No response generated."
            except Exception as e:
                answer= f"Error while generating response:\n\n{e}"      

            st.markdown(answer)


    # Optional formatting

    if not reasoner.requires_full_papers(intent):

        answer = formatter.format_response(
            answer,
            results["metadatas"][0]
        )["answer"]
    
    st.session_state.messages.append(
    {
        "role": "assistant",
        "content": answer
    }
)
    # Show assistant message immediately

    # with st.chat_message("assistant", avatar="🤖"):
    #     with st.spinner("Gemma is analyzing the papers..."):
    #         st.markdown(answer)

    # st.session_state.messages.append(
    #     {
    #         "role": "assistant",
    #         "content": answer
    #     }
    # )



    # ===================================
# -----------------------------------------
# Footer
# -----------------------------------------

# ui.footer()