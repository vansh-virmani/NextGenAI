import streamlit as st
# from predict import predict_intent

st.set_page_config(page_title='ML Chatbot')
st.title("ML Powered chatbot")

st.write("chatbot with intent...")

user_input=st.text_input("Enter something...")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
if st.button("send"):
    if user_input.strip() != "":

        st.session_state.chat_history.append("You ...")