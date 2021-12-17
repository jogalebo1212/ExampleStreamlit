import streamlit as st

st.title("Servidor de prueba")
st.info("Este servidor es para checar los datos que queremos enviar")

st.text("Parte de revisión de apartado de texto")

status = st.radio("Quieres una coca?", ("Sí", "No"))

if status == "Sí":
	st.success("Ah, ok!")
else:
	st.error("Que bueno jeje")
