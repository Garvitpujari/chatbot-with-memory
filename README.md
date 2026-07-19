# 🧠 Chatbot with Persistent Memory

A conversational AI chatbot built using **LangGraph**, **LangChain**, **Groq Llama 3.3**, **Streamlit**, and **SQLite**. The chatbot maintains persistent conversation history, allowing users to continue previous chats seamlessly.

🌐 **Live Demo:** https://chatbot-with-memory-by-garvit.streamlit.app/

---

## ✨ Features

- 💬 AI-powered conversations using Groq Llama 3.3 70B
- 🧠 Persistent conversation memory with LangGraph Checkpointing
- 📂 Multiple chat threads
- 🔄 Switch between previous conversations
- ➕ Start new chats instantly
- ⚡ Fast responses powered by Groq
- 🎨 Simple and responsive Streamlit interface

---

## 🛠️ Tech Stack

- LangGraph
- LangChain
- Groq API
- Streamlit
- SQLite
- Python

---

## 📂 Project Structure

```
chatbot-with-memory/
│
├── streamlit_frontend_database.py
├── langgraph_database_backend.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Garvitpujari/chatbot-with-memory.git
cd chatbot-with-memory
```

Create and activate a virtual environment:

**Windows**

```bash
python -m venv myenv
myenv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv myenv
source myenv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run streamlit_frontend_database.py
```

---

## 🧠 Memory Management

The chatbot uses **LangGraph's SQLite Checkpointer** to maintain conversation history.

Each conversation is assigned a unique **Thread ID**, enabling users to:

- Continue previous conversations
- Switch between chat sessions
- Preserve context across messages

---

## 🚀 Live Demo

https://chatbot-with-memory-by-garvit.streamlit.app/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Garvit Pujari**

GitHub: https://github.com/Garvitpujari
