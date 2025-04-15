import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar matriz de impacto cruzado
cim = pd.read_excel("data/datos_CIM.xlsx", index_col=0).fillna(0)

# Cálculo de métricas
influencia_total = cim.sum(axis=1)
dependencia_total = cim.sum(axis=0)
autonomia = influencia_total - dependencia_total

# Ranking visual por influencia
st.title("📊 Decision Support System - Reúso de Água")

st.subheader("🏆 Ranking de Barreras por Influencia Total")
fig1 = px.bar(influencia_total.sort_values(ascending=False), orientation='h',
              labels={'value': 'Influencia Total', 'index': 'Barrera'},
              color=influencia_total.sort_values(ascending=False),
              color_continuous_scale='Bluered')
st.plotly_chart(fig1)

# Ranking visual por autonomía
st.subheader("⚙️ Ranking por Autonomía Estratégica")
fig2 = px.bar(autonomia.sort_values(ascending=False), orientation='h',
              labels={'value': 'Autonomía Estratégica', 'index': 'Barrera'},
              color=autonomia.sort_values(ascending=False),
              color_continuous_scale='Viridis')
st.plotly_chart(fig2)

# Análisis individual
st.subheader("🔍 Análisis de Influencia Directa")
barrera_seleccionada = st.selectbox("Selecciona una barrera:", cim.index)
impactos = cim.loc[barrera_seleccionada]
st.write("Influencia ejercida por", barrera_seleccionada)
st.dataframe(impactos[impactos > 0].sort_values(ascending=False))

