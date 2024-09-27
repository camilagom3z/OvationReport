import streamlit as st
import pandas as pd
from annotated_text import annotated_text

st.title('Chequeo Ovation DCS')

with st.sidebar:

    option = st.selectbox(
    "Inspección de estaciones de trabajo",
    ("160", "164", "166", "200", "212", "213", "214", "230", "233", "234"),)
annotated_text("Inspección de la estación de trabajo ",(f" {option} ","","#bf6b6b"))
form = st.form(key='my-form')

df = pd.DataFrame(
    [
       {"Item": "El equipo está encendido", "Estado": False, },
       {"Item": "Los dos cables de red se encuentran encendidos y funcionales", "Estado": False},
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