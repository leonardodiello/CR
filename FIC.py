import streamlit as st

st.set_page_config(
    page_title="Calculadora de CR",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("Calculadora de CR")
st.write("Calcule seu Coeficiente de Rendimento de forma simples.")

qtd_materia = st.number_input(
    "Quantas matérias você tem?",
    min_value=1,
    step=1
)

nota_cont = 0.0
ch = 0

for i in range(qtd_materia):
    st.subheader(f"Matéria {i + 1}")

    col1, col2 = st.columns(2)

    with col1:
        nota = st.number_input(
            f"Média da {i + 1}ª matéria",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key=f"nota_{i}"
        )

    with col2:
        carga_horaria = st.number_input(
            f"Carga horária da {i + 1}ª matéria",
            min_value=1,
            step=1,
            key=f"ch_{i}"
        )

    nota_cont += nota * carga_horaria
    ch += carga_horaria

st.divider()

periodo = st.radio(
    "Esse é o seu primeiro período?",
    ["Sim", "Não"]
)

if periodo == "Sim":

    if ch > 0:
        cr = nota_cont / ch

else:

    cr_antigo = st.number_input(
        "Digite seu CR antigo",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    cr = ((nota_cont / ch) + cr_antigo) / 2

st.divider()

st.metric(
    label="CR Atual",
    value=f"{cr:.2f}"
)