# 📊 Tablero Analítico de Ventas — TechSales

Dashboard interactivo desarrollado en **Python con Streamlit** para analizar el rendimiento comercial de un e-commerce durante sus últimos 6 meses de operación.

---

## 🗂️ Estructura del Proyecto

```
📁 Tablero Python de Ventas - Data Analysis/
├── Taller.py                                    # Aplicación principal de Streamlit
├── Taller.ipynb                                 # Notebook de exploración y análisis previo
├── Ventas TeachSales.csv                        # Dataset fuente (separado por ';')
├── Caso de Estudio E-commerce TechSales.pdf     # Documento del caso de estudio
└── README.md
```

> 📄 El archivo **`Caso de Estudio E-commerce TechSales.pdf`** contiene el enunciado y contexto académico del proyecto.

---

## 📌 Descripción

El tablero presenta visualizaciones clave sobre las ventas del e-commerce **TechSales**, dividido en dos secciones principales:

### Visión General

| Gráfico | Descripción |
|---|---|
| **a) Ingresos vs Volumen por Categoría** | Barplot comparando monto total y número de transacciones por categoría |
| **b) Distribución por Región** | Gráfico circular con el porcentaje de ingresos por región geográfica |
| **c) Tendencia Acumulada** | Líneas de ventas acumuladas en el tiempo, desglosadas por categoría |

### Visión Detallada

| Gráfico | Descripción |
|---|---|
| **d/e) Dispersión Interactiva** | Scatter plot (Plotly) con monto vs fecha, identificación de productos al pasar el cursor y detección visual de anomalías |

---

## 🛠️ Tecnologías Utilizadas

| Librería | Uso |
|---|---|
| `streamlit` | Framework del dashboard web |
| `pandas` | Carga, limpieza y agrupación de datos |
| `matplotlib` | Base de renderizado de gráficos estáticos |
| `seaborn` | Gráficos de líneas y barras con estilos |
| `plotly.express` | Gráfico de dispersión interactivo |

---

## ▶️ Cómo Ejecutar

1. Instala las dependencias:

```bash
pip install streamlit pandas matplotlib seaborn plotly
```

2. Asegúrate de que `Ventas TeachSales.csv` esté en la misma carpeta que `Taller.py`.

3. Ejecuta el dashboard:

```bash
streamlit run Taller.py
```

---

## 📁 Dataset

El archivo `Ventas TeachSales.csv` contiene las siguientes columnas:

| Columna | Descripción |
|---|---|
| `Fecha` | Fecha de la venta (formato DD/MM/YYYY) |
| `Categoria` | Categoría del producto |
| `Producto` | Nombre del producto |
| `Monto_Venta` | Monto de la transacción en dólares |
| `Region` | Región geográfica de la venta |

> **Separador:** `;` | **Codificación:** UTF-8
