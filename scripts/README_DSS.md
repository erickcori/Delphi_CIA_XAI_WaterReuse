
# 🧠 Decision Support System (DSS) - Reúso de Agua Residual

Este módulo ofrece una interfaz interactiva en Streamlit para visualizar la **influencia y autonomía estratégica** de cada barrera identificada en la matriz de impacto cruzado (CIM), como apoyo a la toma de decisiones sobre el reúso de aguas residuales en agricultura.

## 📂 Estructura esperada

Asegúrate de tener la siguiente estructura de carpetas y archivos:

```
Delphi_CIA_XAI_WaterReuse/
├── data/
│   └── datos_CIM.xlsx         # ✅ Matriz de impacto cruzado
├── scripts/
│   └── app_dss.py             # ✅ Este script
│   └── README_DSS.md          # 📘 Este archivo de ayuda
```

## 🚀 Cómo ejecutar el DSS

### 1. Instalar dependencias (si no lo has hecho aún)

```bash
pip install streamlit pandas plotly openpyxl
```

### 2. Ejecutar el DSS desde terminal

Desde el directorio principal del proyecto (`Delphi_CIA_XAI_WaterReuse`), ejecuta:

```bash
streamlit run scripts/app_dss.py
```

👉 Esto abrirá el navegador en: `http://localhost:8501`

---

## 📊 Funcionalidades

### 🔸 Ranking por Influencia Total
Visualiza qué barreras ejercen más impacto sobre otras en la matriz CIM.

### 🔸 Ranking por Autonomía Estratégica
Evalúa cuáles barreras son más autónomas y menos dependientes.

### 🔍 Análisis Individual
Permite seleccionar una barrera específica y ver sobre qué otras tiene influencia directa.

---

## 📌 Notas importantes

- El archivo `datos_CIM.xlsx` **debe estar en la carpeta `data/`**.
- El nombre del archivo debe escribirse **exactamente igual** (respetando mayúsculas/minúsculas).
- Puedes modificar el archivo Excel para adaptar el DSS a otros contextos (solo conserva el formato de la matriz).

---

## 👨‍💻 Autor

Desarrollado por **Erick Corimanya**  
🔗 [LinkedIn](https://www.linkedin.com/in/mcorimanya)

---

## 🛡️ Licencia

Este módulo está bajo licencia MIT. Libre uso y adaptación con atribución.
