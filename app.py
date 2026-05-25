import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from datetime import datetime, timezone


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)
db = client["chat"]
collection = db["user"]
user_id = "user_123"  # In a real application, this would be dynamic based on the logged-in user

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Biochemistry expert bot, give me the proper answer"),
        ("user", "{question}")
    ]
)
llm = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-20b")
chain = prompt | llm


def get_history(user_id):
    chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []

    for chat in chats:
        history.append((chat["role"], chat["message"]))
    return history

while True:
    question = input("Ask a question: ")
    if question.lower() in ["exit", "quit"]:
        break
    history = get_history(user_id)

    response = chain.invoke({"history": history, "question": question})

    collection.insert_one({
        "user_id": user_id,
        "role": "user",
        "message": question,
        "timestamp": datetime.now(timezone.utc)
    })
    
    collection.insert_one({
        "user_id": user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.now(timezone.utc)
    })
    print(response.content)

#To convert utc timestamp to IST, you can use the following code snippet:
# from datetime import datetime
# from zoneinfo import ZoneInfo

# # Your timestamp
# timestamp_str = "2026-05-23T09:59:40.925+00:00"

# # Convert to IST
# utc_time = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
# ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

# print(ist_time.strftime("%Y-%m-%d %I:%M:%S %p IST"))  
# # Output: 2026-05-23 03:29:40 PM IST