
        
from langchain_text_splitters import RecursiveCharacterTextSplitter

class PDFTextSplitter:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    # FIXED: This must align with __init__ to be a proper class method
    def split_text(self, text):
        chunks = self.splitter.split_text(text)
        return chunks
