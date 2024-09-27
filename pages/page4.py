import streamlit as st
import pandas as pd
from annotated_text import annotated_text

st.title('Chequeo Ovation DCS')

with st.sidebar:

    option = st.selectbox(
    "Drops y servidores",
    ("Drop 160", "Drop 164", "Scanner 233", "Scanner 166"),)

annotated_text("Revisión de históticos y eventos de Windows " ,(f"{option}", "", "#7029ff"),)
form = st.form(key='my-form')

df = pd.DataFrame(
    [
       {"Item": "Compruebe el Historian Status Monitor ¿Todo se encuentra en orden?", "Estado": False, },
       {"Item": "Rendimiento óptimo del sistema", "Estado": False},
       {"Item": "El cableado del equipo se encuentra en buenas condiciones", "Estado": False},
       {"Item": "La sincronización horaria es la correcta con el GPS", "Estado": False},
    ]
)
edited_df = form.data_editor(df)

txt = form.text_area(
    "Observaciones",
)
submit = form.form_submit_button('Submit')

if submit:
    st.balloons()
    st.write(f'¡Se ha registrado exitosamente la inspección de la estación de trabajo {option}!')


# Ayuda con st.expander
with st.expander("Ayuda"):
    st.write("""
    Para confirmar el rendimiento del sistema abra el Administrador de tareas de Windows:
             
             Ctrl + Alt + Supr -> Administrador de tareas de Windows
    
             
    - Revise la utilización de espacio en disco.
    - Revise el uso, configuración y ubicación de la memoria física y virtual.
    - Compruebe el monitor de rendimiento     
    
    Asegúrese de ingresar cualquier irregularidad o problema detectado para su posterior análisis.
    """)