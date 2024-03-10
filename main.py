import streamlit as st
import pdf_processor as pp
import word_processor as wp
import excel_processor as ep
import website_processor as webp


def main():
    st.title("RAGPro")
    with st.sidebar:
        st.title("Knowledge Base")
        options=["PDF", "Word", "Excel", "Website"]
        checked_options=[st.checkbox(label=option, value=False) for option in options]
        for option, selected in zip(options, checked_options):
            if selected:
                #call processor functions
                st.write(option)


               
    
if __name__=="__main__": 
    main()
    