import streamlit as st
import pandas as pd

st.title('Chequeo Ovation DCS')

st.subheader("Red Ovation")

st.markdown("Anote los hallazgos encontrados en el :blue-background[System Viewer] y :green-background[System Status]")
form = st.form(key='my-form')

txt = form.text_area(
    "Descripción de los hallazgos:",
)
submit = form.form_submit_button('Submit')

if submit:
    st.balloons()
    st.write('¡Se ha registrado exitosamente la inspección de la red Ovation!')

# Ayuda con st.expander
with st.expander("Ayuda"):
    st.write("""
    En esta sección, puede anotar los hallazgos encontrados en el System Viewer y System Status.
    
    - **System Viewer**: Es una herramienta para monitorear los sistemas en tiempo real.
    - **System Status**: Proporciona el estado actual del sistema.
    
    Asegúrese de ingresar cualquier irregularidad o problema detectado para su posterior análisis.
    """)