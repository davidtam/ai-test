import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


load_dotenv()

MODEL_LIST = sorted(["gemma2", "llama3.2", "mistral-nemo", "qwen2.5"])


def ask_question_sbs(question: str, model_name: str = "llama3.2") -> str:

    template = """Question: {question}
                  Answer: Let's think step by step."""
    llm_prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model=model_name)
    chain = llm_prompt | model
    output = chain.invoke({"question": question})

    print(f"{question=}")
    print(f"{output=}")

    return output


if __name__ == "__main__":

    print("Starting streamlit app...")
    st.title("Echo Bot")
    option = st.selectbox(
        "Please select who you want to chat to?",
        MODEL_LIST,
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        output = ask_question_sbs(prompt, option)

        response = f"{option}: {output}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
