import streamlit as st
from services.api_client import add_purchase, bulk_upload_purchases

def render_upload_tab():
    st.header("Upload Purchases")
    
    # Dividir la página en dos columnas
    col_single, col_bulk = st.columns(2)
    
    with col_single:
        # Subida de registro único
        st.subheader("Add a Single Purchase")
        with st.form("single_purchase_form"):
            customer_name = st.text_input("Customer Name")
            country = st.text_input("Country")
            purchase_date = st.date_input("Purchase Date")
            amount = st.number_input("Amount", min_value=0.0)
            
            if st.form_submit_button("Submit"):
                purchase_data = {
                    "customer_name": customer_name,
                    "country": country,
                    "purchase_date": purchase_date.isoformat(),
                    "amount": amount,
                }
                response = add_purchase(purchase_data)
                if response:
                    st.success("Purchase added successfully!")
                else:
                    st.error("Failed to add purchase.")
    
    with col_bulk:
        # Subida de archivo CSV para carga masiva
        st.subheader("Bulk Upload Purchases")
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        if uploaded_file is not None:
            if st.button("Upload CSV"):
                response = bulk_upload_purchases(uploaded_file)
                if response:
                    st.success("Bulk upload successful!")
                else:
                    st.error("Failed to upload CSV.")