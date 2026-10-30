import streamlit as st

st.title("🔒 Verificação de Senha")
st.write(
    "Digite a senha abaixo para ver se você consegue acessar o programa!"
)

# Caixa de texto que esconde os caracteres como senha de verdade
senha = st.text_input("Digite sua senha:", type="password")

# Botão para enviar
if st.button("Verificar Senha"):
  if senha == "pipoca doce":
    st.success("Acertouuu, você acessou o meu coração, amor. Eu te amo mil milhões, coração")
    st.balloons()  # Um efeito legal na tela
    # Aqui você coloca o resto do seu programa
    st.write("O programa continua rodando aqui...")
  else:
    st.error("❌ Senha incorreta! Tente novamente.")