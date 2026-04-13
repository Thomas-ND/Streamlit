import streamlit as st
import pandas as pd

pagina = st.sidebar.radio(
    "Menu",
    ['Inicio', 'Login/Cadastro', 'Dispositivos/Contatos', 'Localização']
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
            st.image("Imagem.jpeg")
        with col2:
            animar_texto("Pulseira estilo smartwatch discreta com botão ao lado, carregamento via USB-C, sensor de batimentos cardiacos para cancelar o gps após sinal enviado caso os batimentos desapareçam.")

elif pagina == "Login/Cadastro":
    st.title("Portal do Usuário")

    if st.session_state["conectado"]:
        st.success(f"Olá, {st.session_state['usuario_nome']}! Você está logado.")
        if st.button("Sair da Conta"):
            st.session_state["conectado"] = False
            st.rerun()
    else:
        aba_login, aba_cadastro = st.tabs(["Entrar", "Criar Conta"])

        # --- FORMULÁRIO DE LOGIN ---
        with aba_login:
            login_email = st.text_input("Email", key="login_email")
            login_senha = st.text_input("Senha", type="password", key="login_senha")
            
            if st.button("Acessar"):
                user = st.session_state["usuarios"].get(login_email)
                if user and user["senha"] == login_senha:
                    st.session_state["conectado"] = True
                    st.session_state["usuario_nome"] = user["nome"]
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Email ou senha incorretos.")

        # --- FORMULÁRIO DE CADASTRO ---
        with aba_cadastro:
            novo_nome = st.text_input("Nome Completo")
            novo_email = st.text_input("Email")
            nova_senha = st.text_input("Crie uma Senha", type="password")
            confirmar_senha = st.text_input("Confirme a Senha", type="password")

            if st.button("Finalizar Cadastro"):
                if not novo_nome or not novo_email or not nova_senha:
                    st.warning("Preencha todos os campos.")
                elif nova_senha != confirmar_senha:
                    st.error("As senhas não coincidem.")
                elif novo_email in st.session_state["usuarios"]:
                    st.error("Este email já está cadastrado.")
                else:
                    # Salva o novo usuário no "banco" temporário
                    st.session_state["usuarios"][novo_email] = {"nome": novo_nome, "senha": nova_senha}
                    st.success("Conta criada! Agora você pode fazer login.")

elif pagina == "Dispositivos/Contatos":
    st.title("Dispositivos e contatos conectados")
    st.write("Conecte seu dispositivo e contatos confiáveis.")
    tab3, tab4 = st.tabs(["Dispositivos", "Contatos"])
    with tab3:
        if st.button("Adicionar dispositivo", use_container_width=True):
            st.write("Dispositivo não encontrado.")
    with tab4:
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Adicionar contatos", use_container_width=True):
                st.write("Selecione os contatos")
        
        with col4:
            st.markdown("<h3 style='text-align: center;'>Atenção</h3>", unsafe_allow_html=True)
            st.write("Selecione apenas os contatos mais confiaveis e dispostos para agir em casos de emergência.")

       


elif pagina == "Localização":
    st.title("Localização via OpenStreetMap")
    df = pd.DataFrame({
    "lat": [-7.845],   # Carpina aprox
    "lon": [-35.254]
    })

    st.map(df)
