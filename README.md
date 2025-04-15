# Delphi_CIA_XAI_WaterReuse
Quantitative assessment of systemic barriers to wastewater reuse in agriculture using an integrated Delphi-CIA approach enhanced with Explainable AI (XAI), network analysis, and Decision Support System (DSS).

# Delphi_CIA_XAI_WaterReuse

🔍 **Evaluación cuantitativa de barreras sistémicas para el reúso de aguas residuales en la agricultura**, usando una combinación de:

- Matriz de Impacto Cruzado (CIA)
- Técnica Delphi
- Interpretabilidad con SHAP (AI explicable)
- Visualizaciones interactivas en Google Colab
- Sistema de Soporte de Decisiones (DSS)

---

## 📁 Estructura del Repositorio

```bash
Delphi_CIA_XAI_WaterReuse/
│
├── data/                   # 📥 Datos de entrada (.xlsx)
│   ├── datos_CIM.xlsx
│
├── figures/                # 📊 Gráficos generados automáticamente
│   ├── shap_summary_multiclase.png
│
├── notebooks/              # 📒 Notebooks de análisis y visualización
│   ├── visualizacion_SHAP.ipynb
│
├── results/                # 📤 Resultados exportados (opcional)
│
├── scripts/                # 🧠 Códigos Python reutilizables
│   ├── shap_analysis.py
│
├── LICENSE                 # Licencia del proyecto
└── README.md               # Este archivo

---

## 📊 Visualización SHAP

🔗 Abre el notebook para visualizar la importancia de barreras por clase:  
[visualizacion_SHAP.ipynb](https://github.com/erickcori/Delphi_CIA_XAI_WaterReuse/blob/main/notebooks/visualizacion_SHAP.ipynb)

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/erickcori/Delphi_CIA_XAI_WaterReuse/blob/main/notebooks/visualizacion_SHAP.ipynb)

Este notebook permite subir tu matriz `datos CIM.xlsx`, aplicar XGBoost y visualizar la importancia de cada barrera para distintas clases con gráficos SHAP.

---

## 📌 Próximos análisis (en preparación)

- 📈 Clustering jerárquico y HDBSCAN
- 🤖 Red neuronal para clasificación de barreras
- 🎯 Análisis de sensibilidad
- 🧠 Sistema DSS con interfaz

---

## 📬 Contacto

Desarrollado por **Erick Corimanya**  
🔗 [LinkedIn](https://www.linkedin.com/in/mcorimanya)

---

## 🛡️ Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
