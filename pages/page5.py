import streamlit as st
import pandas as pd

st.title('Chequeo Ovation DCS')

st.markdown("Ventana :red-background[Error Log] ")
form = st.form(key='my-form')

txt = form.text_area(
    "Anote las anomalías encontradas en la ventana de Error Log",
)
submit = form.form_submit_button('Submit')

if submit:
    st.balloons()
    st.write('¡Ha finalizado exitosamente el chequeo al DCS Ovation!')