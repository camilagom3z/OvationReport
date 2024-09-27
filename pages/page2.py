import streamlit as st
import pandas as pd
from annotated_text import annotated_text



st.title('Chequeo Ovation DCS')

with st.sidebar:
    option = st.selectbox(
    "Inspección de controladores",
    ("118/168", "113/163", "113/163", "117/167", "121/171", "23/73", "33/83", "41/91", "42/92", "44/94", "43/93"), )

annotated_text("Inspección del controlador ",(f"{option}", "", "#ffbd59"),)



form = st.form(key='my-form')

df = pd.DataFrame(
    [
       {"Item": "Led Power (P) en verde", "Estado": False, },
       {"Item": "Led Communicaction (Cm) en verde", "Estado": False},
       {"Item": "Led Control (Ct) en verde", "Estado": False},
       {"Item": "Led Alive (A) en verde", "Estado": False},
       {"Item": "Led Error (E) en rojo", "Estado": False},
       {"Item": "Enlaces de fibra óptica en buen estado", "Estado": False},
       {"Item": "Fuente de alimentación del controlador en buenas condiciones", "Estado": False},
       {"Item": "Fuente de alimentación del controlador en buenas condiciones", "Estado": False},
   ]
)
edited_df = form.data_editor(df)
submit = form.form_submit_button('Submit')

if submit:
    st.balloons()
    st.write(f'¡Se ha registrado exitosamente la inspección del controlador {option}!')

# Ayuda con st.expander
with st.expander("Ayuda"):
    st.image('C:/Users/AuxiliarInstrumentac/Documents/OvationReport/pages/OCR1100.png', caption="OCR 1100")