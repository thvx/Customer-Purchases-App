import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# Importar el cliente de la API
from services.api_client import get_filtered_purchases, get_kpis, get_forecast

def render_analyse_tab():
    st.header("Analyse Purchases")

    col_filters, col_table = st.columns([1,1], gap="large")

    with col_filters:
        st.subheader("Filters")
        start_date = st.date_input("Start Date", value=None)
        end_date = st.date_input("End Date", value=None)
        filter_country = st.text_input("Filter by Country")

        # Botón para aplicar filtros
        if st.button("Apply Filters"):
            if start_date and end_date and start_date > end_date:
                st.error("Error: Start date cannot be greater than end date.")
            else:
                # Llamada a la API para obtener compras filtradas
                purchases = get_filtered_purchases(
                    start_date=start_date.isoformat() if start_date else None,
                    end_date=end_date.isoformat() if end_date else None,
                    country=filter_country if filter_country else None
                )

                # Guardar los resultados en el estado de la sesión
                st.session_state.filtered_purchases = purchases

    with col_table:
        # Mostrar la tabla de resultados
        if "filtered_purchases" in st.session_state:
            purchases = st.session_state.filtered_purchases
            if purchases:
                st.subheader("Filtered Purchases")
                df = pd.DataFrame(purchases)
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("No purchases found with the selected filters.")

    # Mostrar KPIs
    st.subheader("Mean Purchases per Client")
    kpis = get_kpis()

    if kpis:
        # Mostrar el promedio de compras por cliente
        st.subheader(f"${kpis['mean_per_client']:.2f}")

        # Mostrar la cantidad de clientes por país
        st.subheader("Clients per Country")
        
        clients_per_country = kpis["clients_per_country"]
        df_clients = pd.DataFrame(list(clients_per_country.items()), columns=["Country", "Clients"])
        col1, col2 = st.columns([3, 2], gap="large")

        with col1:
            # Crear un mapa con Plotly
            fig = px.choropleth(
                df_clients,
                locations="Country",
                locationmode="country names",
                color="Clients",
                hover_name="Country",
                color_continuous_scale=px.colors.sequential.Plasma,
            )
            st.plotly_chart(fig)

        with col2:
            # Mostrar la tabla de países y cantidad de clientes
            df_clients_table = pd.DataFrame(
                list(clients_per_country.items()), columns=["Country", "Clients"]
            )
            
            st.dataframe(
                df_clients_table,
                height=300,
                use_container_width=True
            )
    else:
        st.warning("No KPIs available.")

    # Mostrar pronóstico de ventas
    st.subheader("Sales Forecast")
    periods = st.number_input("Forecast Period (days)", min_value=1, max_value=365, value=12, step=1)

    if st.button("Generate Forecast"):
        forecast = get_forecast(periods=periods)
        if forecast:
            st.subheader(f"Forecast for the next {periods} days:")
            
            # Convertir el pronóstico a un DataFrame para mejor visualización
            df_forecast = pd.DataFrame(list(forecast.items()), columns=["Date", "Amount"])
            df_forecast["Date"] = pd.to_datetime(df_forecast["Date"])
            
            # Mostrar la tabla de pronóstico
            st.dataframe(df_forecast, use_container_width=True)

            # Mostrar un gráfico de línea con Plotly
            fig = px.line(
                df_forecast,
                x="Date",
                y="Amount",
                title="Sales Forecast",
                labels={"Amount": "Forecasted Sales ($)", "Date": "Date"},
            )
            st.plotly_chart(fig)
        else:
            st.warning("No forecast data available.")
