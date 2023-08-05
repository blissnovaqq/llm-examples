import streamlit as st
from llmflows.llms import OpenAI

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(api_key=openai_api_key)
    result, call_data, model_config = llm.generate(
        prompt="Generate a cool title for an 80s rock song"
    )
    st.info(llm(result))
    st.info(llm(call_data))
    st.info(llm(model_config))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
