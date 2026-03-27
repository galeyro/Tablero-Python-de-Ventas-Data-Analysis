import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("📊 Tablero Analítico de Ventas")
st.markdown("""
**Análisis de Rendimiento Comercial (Últimos 6 meses)**  
Este panel interactivo presenta los datos históricos sobre el desempeño de ventas del E-commerce "TechSales". El objetivo es proveer información visual para analizar los ingresos y apoyar la toma de decisiones.  
*[Descargar CSV de datos fuente](https://udla.brightspace.com/content/enforced/710345-202620-250-ICBS0003-5357_5358_5359/Ventas%20TeachSales.csv)*
""")

# 1. SOLO CARGAR Y LIMPIAR DATOS AQUI
@st.cache_data
def cargar_datos():
    df = pd.read_csv("Ventas TeachSales.csv", sep=';')
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
    df = df.sort_values('Fecha')
    return df

# Obtenemos el DataFrame limpio llamando a la función
df = cargar_datos()

# Agrupaciones y cálculos
df_diario = df.groupby(['Fecha', 'Categoria'])['Monto_Venta'].sum().reset_index()
df_diario['Monto_Acumulado'] = df_diario.groupby('Categoria')['Monto_Venta'].cumsum()
promedios = df.groupby('Categoria')['Monto_Venta'].mean().round(2)
ventas_por_region = df.groupby('Region')['Monto_Venta'].sum()
ventas_totales_cat = df.groupby('Categoria').agg(
    Monto_Venta=('Monto_Venta', 'sum'),
    Cantidad_Ventas=('Monto_Venta', 'count')
).sort_values(by='Monto_Venta', ascending=False).reset_index()


# ==========================================
st.divider()
st.subheader("Visión General")

# Creamos dos columnas (50% de ancho cada una)
col1, col2 = st.columns(2)

# Colocamos el contenido en la primera columna
with col1:
    st.markdown("""
**c) Análisis Temporal y Tendencias:**  
Trayectoria acumulada del monto de ventas mensual desglosado por categoría de producto.
""")

    # 3. CREAR Y MOSTRAR EL GRÁFICO
    # Definimos la figura y la guardamos en la variable 'fig'
    fig1 = plt.figure(figsize=(14, 7))
    sns.set_style("whitegrid")

    # Pintamos el gráfico de Seaborn DENTRO de esa figura
    grafico = sns.lineplot(data=df_diario, x='Fecha', y='Monto_Acumulado', hue='Categoria', marker='o', linewidth=2.5)

    # Personalizaciones de Matplotlib
    plt.title('Ventas Acumuladas vs Promedio por Categoría', fontsize=16)
    plt.xlabel('Fecha de Venta', fontsize=12)
    plt.ylabel('Monto ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Categorías', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # ¡LA MAGIA DE STREAMLIT AQUI!
    # Reemplazamos el antiguo plt.show() por st.pyplot() pasándole la figura
    st.pyplot(fig1)

    # ========================================================================
    st.markdown("""
**a) Ventas por Categoría (Ingresos vs Volumen):**  
Comparativa entre el monto total de ingresos y la cantidad de transacciones generadas por cada categoría.
""")
    fig3 = plt.figure(figsize=(10,6))
    sns.set_style("whitegrid")

    grafico_barras = sns.barplot(
        data = ventas_totales_cat,
        x="Categoria",
        y="Monto_Venta",
        palette="viridis",
        hue="Categoria",
        legend=False
    )
    # --- Añadir los valores en el gráfico ---
    # Usamos enumerate para saber en qué barra estamos y sacar el dato de 'Cantidad_Ventas'
    for i, p in enumerate(grafico_barras.patches):
        # Valor en el Eje Y (Monto total) - Se mantiene ARRIBA de la barra
        grafico_barras.annotate(f'${p.get_height():,.0f}', 
                                (p.get_x() + p.get_width() / 2., p.get_height()), 
                                ha = 'center', va = 'center', 
                                xytext = (0, 9), 
                                textcoords = 'offset points',
                                fontsize=11, fontweight='bold')
        
        # Valor del Conteo (Cantidad de ventas) - Se muestra DENTRO de la barra
        cantidad = ventas_totales_cat.iloc[i]['Cantidad_Ventas']
        grafico_barras.annotate(f'{cantidad} ventas', 
                                (p.get_x() + p.get_width() / 2., p.get_height() / 2), 
                                ha = 'center', va = 'center', 
                                color='white', fontsize=12, fontweight='bold')
    # Etiquetas y personalización
    plt.title('Ingresos Totales y Cantidad de Ventas por Categoría', fontsize=15, fontweight='bold')
    plt.xlabel('Categoría', fontsize=12)
    plt.ylabel('Ventas Totales ($)', fontsize=12)
    plt.ylim(0, ventas_totales_cat['Monto_Venta'].max() * 1.15) 
    plt.tight_layout()
    
    # 3. Mandarlo a la web de Streamlit (reemplaza plt.show())
    st.pyplot(fig3)

    # ========================================================================
# Colocamos el contenido en la segunda columna
with col2:

    st.markdown("""
**b) Rendimiento del Mercado por Región:**  
Distribución porcentual de los ingresos totales generados en cada una de las regiones geográficas.
""")
    
    # 3. CREAR Y MOSTRAR EL GRÁFICO
    # Definimos la figura y la guardamos en la variable 'fig'
    fig2 = plt.figure(figsize=(14, 7))
   
    # Definir colores elegantes
    colores = sns.color_palette('pastel')[0:3]

    # Crear el gráfico circular
    plt.pie(ventas_por_region, 
            labels = ventas_por_region.index, 
            autopct = '%1.2f%%',           # Muestra el porcentaje con 1 decimal
            startangle = 140,              # Gira el gráfico para mejor visualización
            colors = colores,              # Usar nuestra paleta de colores
            explode = (0.05, 0, 0),        # "Saca" un poquito la primera rebanada para resaltar
            shadow = True)                 # Añade una sombra sutil

    # Título del gráfico
    plt.title('Distribución de Ventas Totales por Región', fontsize=14, fontweight='bold')

    # ¡LA MAGIA DE STREAMLIT AQUI!
    # Reemplazamos el antiguo plt.show() por st.pyplot() pasándole la figura
    st.pyplot(fig2)

# ==========================================
st.divider()
st.subheader("Visión Detallada de Elementos")

st.markdown("""
**d y e) Visión Detallada: Producto Estrella y Detección de Anomalías:**  
Gráfico de dispersión interactivo que detalla la relación diaria entre montos de venta e identifica productos específicos con el cursor.
""")

# Definimos tu paleta de 4 colores con alto contraste
mis_colores = ['#E63946', '#1D3557', '#2A9D8F', '#F4A261']

# Se crea el gráfico (lo guardamos en fig4 por orden)
fig4 = px.scatter(df, 
                 x='Fecha', 
                 y='Monto_Venta', 
                 color='Categoria', 
                 hover_name='Producto', 
                 title='Ventas: Monto vs Fecha por Categoría',
                 labels={'Monto_Venta': 'Monto Total ($)', 'Fecha': 'Fecha de Venta'},
                 template='plotly_white', # Fondo blanco
                 color_discrete_sequence=mis_colores) # Aplicamos tus 4 colores

# Ajuste para resaltar más los puntos
fig4.update_traces(marker=dict(size=14, opacity=0.9, line=dict(width=1.5, color='white')))

# ¡LA MAGIA DE STREAMLIT AQUI para Plotly!
# Reemplazamos fig.show() por st.plotly_chart() e incluimos theme=None para forzar el fondo blanco
st.plotly_chart(fig4, use_container_width=True, theme=None)

