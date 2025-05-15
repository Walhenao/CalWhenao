import streamlit as st

st.set_page_config(
    page_title="Calculadora Web",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar con título y opciones
with st.sidebar:
    st.title("Menú")
    st.write("Opciones disponibles:")

    limpiar_historial = st.button("Limpiar Historial")
    descargar_historial = st.button("Descargar Historial")

    st.markdown("---")
    st.subheader("Instrucciones")
    st.write("""
    - Escribe operaciones matemáticas en la caja principal.  
    - Usa operadores: +, -, *, /, **, ()  
    - Ejemplo: (2 + 3) * 5  
    - Haz click en 'Calcular' para ver el resultado.  
    """)

# Título principal centrado y estilizado
st.markdown(
    """
    <h1 style='text-align: center; color: #1F4E79; font-family: Arial Black, sans-serif;'>
        CALCULADORA WEB
    </h1>
    <hr style='border: 1px solid #1F4E79;'>
    """,
    unsafe_allow_html=True
)

# Entrada y botón en columnas
col1, col2 = st.columns([3,1])

with col1:
    operacion = st.text_input("Escribe la operación matemática:", "", placeholder="Ej: (2 + 3) * 5")

with col2:
    calcular = st.button("Calcular")

# Historial sesión
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Limpiar historial si se pide
if limpiar_historial:
    st.session_state.historial = []  # Limpiamos el historial

if calcular:
    try:
        resultado = eval(operacion)
        st.success(f"Resultado: {resultado}")
        st.session_state.historial.append(f"{operacion} = {resultado}")
    except Exception as e:
        st.error(f"Error en la operación: {e}")

st.markdown("---")

# Mostrar historial solo si se hace clic en el botón
if descargar_historial:
    if st.session_state.historial:
        st.subheader("Historial de operaciones:")
        for op in reversed(st.session_state.historial):
            st.write(op)

        historial_str = "\n".join(st.session_state.historial)
        st.download_button(
            label="Descargar historial",
            data=historial_str,
            file_name="historial_calculadora.txt",
            mime="text/plain"
        )
    else:
        st.write("No hay historial de operaciones.")


