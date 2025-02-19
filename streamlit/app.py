import streamlit as st
from presentation.upload_tab import render_upload_tab
from presentation.analyse_tab import render_analyse_tab

def main():
    st.title("Customer Purchases App")
    tab1, tab2 = st.tabs(["Upload", "Analyse"])
    
    with tab1:
        render_upload_tab()
    
    with tab2:
        render_analyse_tab()

if __name__ == "__main__":
    main()