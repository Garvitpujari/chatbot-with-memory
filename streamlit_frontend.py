import streamlit as st 
from langgraph_backend import chatbot
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage , BaseMessage
# but normally m doosre message pe phle ud gaye jitni bar enter y poori script re execute
# st -> session state  , jab enter press karte hai to iske andar ki chije erase nhi hoti jab page refresh karenge tb hi udegi 

# normal message history ki empty list m li to gayab hojyga


CONFIG={'configurable':{'thread_id':'thread-1'}}

if 'message-history' not in st.session_state:
    st.session_state['message-history']=[]

for message in st.session_state['message-history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input=st.chat_input('Type here')


if user_input :
    st.session_state['message-history'].append({'role':'user', 'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

        

    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    ai_message=response['messages'][-1].content

    st.session_state['message-history'].append({'role':'assistant', 'content':user_input})
    with st.chat_message('assistant'):
        st.text(ai_message)


