
# shap_analysis.py
# Análisis SHAP para matriz de impacto cruzado Delphi-CIA

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from xgboost import XGBClassifier
import shap
import matplotlib.pyplot as plt
import os

# Crear carpeta de salida si no existe
os.makedirs("figures", exist_ok=True)

# 1. Cargar y normalizar matriz de impacto cruzado
cim = pd.read_excel("data/datos_CIM.xlsx", index_col=0).fillna(0)

scaler = MinMaxScaler()
cim_normalized = pd.DataFrame(scaler.fit_transform(cim),
                              index=cim.index,
                              columns=cim.columns)

# 2. Crear variable de salida (barrera más influyente por fila)
y = cim_normalized.idxmax(axis=1)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 3. Entrenar modelo XGBoost
model = XGBClassifier(learning_rate=0.01, max_depth=3)
model.fit(cim_normalized, y_encoded)

# 4. Calcular valores SHAP
explainer = shap.Explainer(model)
shap_values = explainer(cim_normalized)

# 5. Graficar SHAP summary plot mejorado
shap.summary_plot(
    shap_values,
    cim_normalized,
    plot_type="bar",
    class_names=le.classes_,
    show=False
)

plt.gcf().set_size_inches(10, 6)
plt.title("Importancia de barreras por clase (SHAP)", fontsize=16)
plt.xlabel("Impacto medio (SHAP)", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()

# 6. Guardar gráfico
plt.savefig("figures/shap_summary_multiclase.png", dpi=300)
plt.close()

print("✅ Gráfico SHAP guardado en 'figures/shap_summary_multiclase.png'")
