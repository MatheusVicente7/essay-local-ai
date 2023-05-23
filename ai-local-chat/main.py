import streamlit
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
#https://www.youtube.com/watch?v=IaTiyQ2oYUQ

def init():
    load_dotenv()

    # test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    streamlit.set_page_config(page_title="Local Chat")
    streamlit.header("Chat")


def main():
    init()

    chat = ChatOpenAI(temperature=0)
    #act like state of React
    if "messages_schema" not in streamlit.session_state:
        streamlit.session_state.messages_schema = [
            # SystemMessage == Instructions do the Model what is he supposed to be
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=input),
        ]

    with streamlit.sidebar:
        user_input = streamlit.text_input("Your message: ", key="user_input")

    if user_input:
        message(user_input, is_user = True)
        streamlit.session_state.messages_schema.append(HumanMessage(content=user_input))
        with streamlit.spinner("Thinking"):
            response = chat(streamlit.session_state)
        streamlit.selectbox.messages_schema.append(AIMessage=response.content)
        message(response.content, is_user = False)
    state_messages = streamlit.get('messages', [])
    for i, msg in enumerate(state_messages[1:]):
            if i % 2 == 0:
                message(msg.content, is_user = True, key=str(i) + '_user')
            else: 
                message(msg.content, is_user = False, key=str(i) + '_ia')

if __name__ == "__main__":
    main()
