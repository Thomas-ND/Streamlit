import streamlit as st
import pandas as pd


pagina = st.sidebar.radio(
    "Menu",
    ['Inicio', 'Localização']
)

st.markdown("""
<style>
@keyframes aparecer {
    from {opacity: 0;}
    to {opacity: 1;}
}

.animado {
    opacity: 0;
    transform: translateY(20px);
    animation: aparecer 1s ease-in-out forwards;
    font-size: 24px;
}
</style>
""", unsafe_allow_html=True)

def animar_texto(texto):
    st.markdown(f'''
    <div style="
        opacity:0;
        animation: aparecer 1s ease-in-out forwards;
    ">
        {texto}
    </div>
    ''', unsafe_allow_html=True)

if pagina =="Inicio":

    st.title("AegisSync")
    st.write("Segurança que reage com você.")

    tab1, tab2 = st.tabs(["Apresentação", "Produto"])

    with tab1:
        animar_texto("Em situações de perigo, cada segundo importa. Muitas vezes, a dificuldade não é pedir ajuda, mas conseguir fazer isso a tempo. Pensando nisso, foi desenvolvido o AegisSync, uma pulseira inteligente que conecta o usuário a um sistema de segurança em tempo real.")
    with tab2:
        col1, col2 = st.columns(2)

        with col1: 
            st.image("imagem.jpeg")
        with col2:
            animar_texto("Pulseira estilo smartwatch discreta com botão ao lado, carregamento via USB-C, sensor de batimentos cardiacos para cancelar o gps após sinal enviado caso os batimentos desapareçam.")

elif pagina == "Localização":
    st.title("Localização via StreetOpenMap")
    df = pd.DataFrame({
    "lat": [-7.845],   # Carpina aprox
    "lon": [-35.254]
    })

    st.map(df)