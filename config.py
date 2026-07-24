from pathlib import Path
import streamlit as st
BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR /"data"/"uploaded_papers"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

print(f"Upload directory is set to: {UPLOAD_DIR}")
print(UPLOAD_DIR.exists())



st.set_page_config(
    page_title="Research Helper AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)