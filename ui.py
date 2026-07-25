import streamlit as st
from modules.chroma_manager import ChromaManager

db=ChromaManager()

class UI:
    def load_css(self):
        st.markdown(
            """
                    <style>
                    
                    
        /* Hide Streamlit menu */
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        

        /* Main Page */
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            padding-left:3rem;
            padding-right:3rem;
        }

        /* Hero Title */
        .hero-title{
            font-size:48px;
            font-weight:800;
            text-align:center;
            color:#4F8BF9;
            margin-bottom:10px;
        }

        /* Hero Subtitle */
        .hero-subtitle{
            font-size:20px;
            text-align:center;
            color:#B8B8B8;
            margin-bottom:35px;
        }

        /* Card */
        .custom-card{
            background-color:#1E1E1E;
            padding:20px;
            border-radius:15px;
            border:1px solid #2E2E2E;
            margin-bottom:20px;
        }

        /* Answer Box */
        .answer-box{
            background:#1E1E1E;
            padding:25px;
            border-radius:15px;
            border-left:6px solid #4F8BF9;
        }

        /* Source Box */
        .paper-box{
            background:#1E1E1E;
            padding:15px;
            border-radius:12px;
            border-left:5px solid #2ECC71;
            margin-bottom:10px;
        }
                    
                    
                    </style>
                    """,
            unsafe_allow_html=True,
        )

    def show_header(self):

        st.markdown(
            """
                        
                        <div class="hero-title">
                        Your AI Research Helper.
                        </div>
                        
                        
                        """,
            unsafe_allow_html=True,
        )
        st.info("Upload one or more research papers and ask questions naturally.")

    # sidebar
    def show_sidebar(self, uploaded_files,db):
        with st.sidebar:
            st.title("📚 AI Research Helper ")
            st.divider()

            st.subheader("📄 Uploaded Papers")
            if uploaded_files:
                for pdf in uploaded_files:
                    st.success(pdf.name)

            else:
                st.info("No papers uploaded.")

            st.divider()
            st.subheader("📊 Statistics")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📄 Papers", len(uploaded_files) if uploaded_files else 0)

            

            with col2:
   
                total_size = sum(file.size for file in uploaded_files) / (1024 * 1024) if uploaded_files else 0
                st.metric("💾 Size", f"{total_size:.2f} MB")

            st.divider()

            st.subheader("💡 Example Questions")

            st.markdown("""
- Compare these papers
- Summarize this paper
- Find research gaps
- Explain methodology
- Extract limitations
- Suggest future work
- Compare datasets
            """)

            st.divider()
         
                    
            st.subheader("💬Recent Questions")
            
            recent_ques=[
                            
                msg["content"]
                            
                        
                for msg in st.session_state.messages
                if msg["role"] == "user"
                                 
                ][-8:]
            for question in reversed(recent_ques):
                if len(question) > 40:
                    question =question[:40]+ "...."
                                
                st.markdown(f"• {question}")  
                
            st.divider()    
                
          
         
            
            col1, col2 =st.columns(2)
            with col1:
                            
                        
                if st.button("🗑 Clear Chat"):
            
                    st.session_state.messages = []
            
                    st.rerun()
                
            with col2:
                if st.button("🗑Delete Papers"):
            
                    st.session_state.papers = {}
            
                    try:
                        db.clear_database()
                    except:
                        pass
            
                    st.rerun()
            
            if st.button("♻️ Clear Cache"):
                st.cache_data.clear()
                st.cache_resource.clear()
                st.success("Cache cleared!")
                st.rerun()  
            st.divider()    
                        
            st.caption("Powered by Gemma 4")

    # Dashboard

    def show_dashboard(self, papers, chunks, database):
        st.subheader("Dahsboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Papers", papers)

        with col2:
            st.metric("🧩 Chunks", chunks)

        with col3:
            st.metric("💾 Database", database)

    # Upload_section

    def upload_title(self):
        st.subheader("Ask Questions")

    # Ai answer

    def show_answer(self, question, answer):
        st.subheader("AI Answer")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.session_state.chat_history.append({"question": question, "answer": answer})
        for chat in st.session_state.chat_history:
            st.markdown(f"{chat['question']}")
        st.markdown(
            f"""
            <div class="answer-box">
            {answer}
            </div>
            
            
            """,
            unsafe_allow_html=True,
        )

    def show_sources(self, papers):

        st.subheader("📚 Source Papers")

        for paper in papers:

            st.markdown(
                f"""
                <div class="paper-box">
                📄 {paper}
                </div>
                """,
                unsafe_allow_html=True,
            )

    