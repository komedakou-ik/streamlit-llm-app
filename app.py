from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import streamlit as st

st.title("専門家への質問")

st.write("「日々の心身の健康」に関する気になることを入力してください。")
input_message = st.text_input(label="質問内容")

st.write("どの専門分野から意見を聞きたいか選択してください。選択後、質問送付ボタンを押してください。")
selected_item = st.radio("専門分野", ["心理学", "栄養学"])

st.divider()

if st.button("質問送付"):

    if not input_message:
        st.warning("質問内容を入力してください。")
    elif selected_item == "心理学":
        from langchain_openai import ChatOpenAI
        from langchain.schema import SystemMessage, HumanMessage
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content="You are a psychology expert. Please answer questions from the perspective of psychology in an easy-to-understand way."),
            HumanMessage(content=input_message),
        ]
        result = llm(messages)
        st.write(f"ご回答:\n{result.content}")
    elif selected_item == "栄養学":
        from langchain_openai import ChatOpenAI
        from langchain.schema import SystemMessage, HumanMessage
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content="You are a nutrition expert. Please answer questions from the perspective of nutritional science in an easy-to-understand way."),
            HumanMessage(content=input_message),
        ]
        result = llm(messages)
        st.write(f"ご回答:\n{result.content}")

