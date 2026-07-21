import streamlit as st

from config import UPLOAD_DIR
from modules.pdf_loader import PDFLoader
from modules.text_splitter import PDFTextSplitter
from modules.context_extractor import ContextExtractor
from modules.embedding_generator import EmbeddingGenerator

from modules.chroma_manager import ChromaManager
st.set_page_config(page_title="Research Helper AI")

st.title("📚 Research Helper AI")

st.write(
    """
Welcome to AI Research Helper!

This tool allows you to upload your research papers in PDF format, extract the text, and split it into manageable chunks for further analysis or processing.
"""
)


uploaded_files = st.file_uploader(
    "Upload your research papers (PDF format)",
    type=["pdf"],
    accept_multiple_files=True,
    help="You can upload at most 5 PDF files at once. Each file will be processed individually."
)
if uploaded_files and len(uploaded_files) > 5:
    st.error("You can upload at most 5 PDF files at once. Please remove some files and try again.")
    uploaded_files = None  

loader = PDFLoader()
splitter = PDFTextSplitter()
context=ContextExtractor()
embedder=EmbeddingGenerator()
db=ChromaManager()


st.success("connection to vector database established successfully!")

if uploaded_files:

    for pdf in uploaded_files:

        # Save uploaded file
        save_path = UPLOAD_DIR / pdf.name

        with open(save_path, "wb") as f:
            f.write(pdf.getbuffer())

        st.success(f"✅ {pdf.name} uploaded successfully!")

        
        text = loader.extract_text(save_path)

       
        st.subheader(f"📄 {pdf.name}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Characters", len(text))

        with col2:
            st.metric("Words", len(text.split()))

        with col3:
            st.metric("File Size", f"{pdf.size / (1024 * 1024):.2f} MB")

       
        with st.expander("📖 View Extracted Text"):

            st.write(text[:2000])

            if len(text) > 2000:
                st.info("Only the first 2000 characters are displayed.")

        sections=context.detect_sections(text)

        st.header("🔍 Detected Sections")

        if sections:
            for section in sections:
                st.success(f"{section.title()} section detected.")
        else:
            st.warning("⚠️ No predefined sections detected in the text.")                

        chunks = splitter.split_text(text)

        st.success(f"🧩 Total Chunks Created: {len(chunks)}")

        for i, chunk in enumerate(chunks):

            with st.expander(
                f"Chunk {i+1} ({len(chunk)} characters)"
            ):
                st.write(chunk)
                
                # Generate embeddings for the chunk
        embeddings= embedder.generate_embeddings(chunks)   
        
                
        st.success(f"🧠 Embeddings generated for  chunks.")
        st.write({embeddings.shape})
        for i,embedding in enumerate(embeddings):
            
            
                st.write(embeddings[i][:10])  
        #add database
        
        db.add_documents(
            chunks=chunks, embeddings=embeddings, paper_name=pdf.name,)        

        st.success("Stored successfully!")
        st.info(f"Stored collection {db.collection.count()} in the vector database.")