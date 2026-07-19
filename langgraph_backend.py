from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq
from typing import TypedDict,Literal ,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import operator
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage , BaseMessage
from langgraph.checkpoint.memory import MemorySaver

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
    
checkpointer= MemorySaver()

graph=StateGraph(ChatState)

# add nodes
graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)


# block to fetch message
# CONFIG={'configurable':{'thread_id':'thread-1'}}
# response=chatbot.invoke(
#             {'messages':[HumanMessage(content='hi my name is  garvit')]},    
#                 config=CONFIG

#         )

# print(chatbot.get_state(config=CONFIG).values['messages'])



# stream=chatbot.stream(
#     {'messages':[HumanMessage(content='what is the receipe to make pasta ')]},    
#     config={'configurable':{'thread_id':'thread-1'}},
#     stream_mode='messages'

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


