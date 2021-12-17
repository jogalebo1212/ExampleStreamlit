import streamlit as st

st.title("Servidor para Gato")
st.info("Es para recordarte que te amo mucho")

st.text("cosa apestosa")

status = st.radio("Me quieres?", ("Sí", "No"))

if status == "Sí":
	st.success("Yo más")
else:
	st.error("Me enoja")