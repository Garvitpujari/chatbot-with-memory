from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq
from typing import TypedDict,Literal ,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import operator
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage , BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
#1 InMemorySaver jo abhi krre  
#2 sqlite saver sqqlite db k upar based used generally ffor prototyping , small database used for making production ready things
#3 Postgre 
load_dotenv()

llm=ChatGroq(model='llama-3.3-70b-versatile')

from langgraph.graph.message import add_messages
class ChatState(TypedDict):

    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):

    # take user query from state 
    messages=state['messages']

    #send to llm 
    response=llm.invoke(messages)

    #return store state 
    return {'messages':[response]}   # meesage list m ayga aur ek sath k saath combine ho jayga 
# ek sqlite db banana padega


import sqlite3
# we ll use multiple thread but sqlite db works on single thread that s why we are marking check same thread as false
# same db ko hum alag alg threads me use karenge aap tension mat lo  
conn=sqlite3.connect(database='chatbot.db',check_same_thread=False)

  
checkpointer= SqliteSaver(conn)

graph=StateGraph(ChatState)

# add nodes
graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)


def retrieve_all_threads():


    all_threads=set()
    for checkpoint in checkpointer.list(None): # overall kitne chkpnts hai not of a particular thread id
        all_threads.add(checkpoint.config['configurable']['thread_id'])


    return(list(all_threads))



# test working in db

# CONFIG = {
#         'configurable': {
#             'thread_id':'thread-2'
#         }
#     }
# # thread change karunga to messagea doosre thread m store hojaynge
# # dekhne ke liye vs code m hi sqlite view install kar lia 
# # har question par 3 baar thread 1 ki entry db me ek start k time ek check node ke pass ek end ke pass 
# # fir puchunga to 3 or honge , doosre thread pe puchunga to uske honge
# # check point me jao double click karo vha p screen ka button ayga vo dabao then we can see message not that clean but can see
# response=chatbot.invoke(
#                 {'messages': [HumanMessage(content=' My name is ankul')]},
#                 config=CONFIG,
#                 stream_mode='messages'
#             )

# print(response)




























# # block to fetch message
# # CONFIG={'configurable':{'thread_id':'thread-1'}}
# # response=chatbot.invoke(
# #             {'messages':[HumanMessage(content='hi my name is  garvit')]},    
# #                 config=CONFIG

# #         )

# # print(chatbot.get_state(config=CONFIG).values['messages'])



# # stream=chatbot.stream(
# #     {'messages':[HumanMessage(content='what is the receipe to make pasta ')]},    
# #     config={'configurable':{'thread_id':'thread-1'}},
# #     stream_mode='messages'

# )
# print(type(stream)) # generator hoga




# backend me koi change nhi karenge frontend m krenge

# for message_chunk , metadata in chatbot.stream(
#     {'messages':[HumanMessage(content='what is the receipe to make pasta ')]},    
#     config={'configurable':{'thread_id':'thread-1'}},
#     stream_mode='messages'

# ):
#     if message_chunk.content :
#         print(message_chunk.content , end=" " ,flush=True)


