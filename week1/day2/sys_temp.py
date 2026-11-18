import os
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq 
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
     raise ValueError("Api Error missing api key")
clinet = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

# system 
role="user"
prompt="suggest a unique name for my podcast channel on youtube only one name suggest me which also contain alok which is my name, how is ALOK SPEAKS  "
message_system={
    "role":"system",
    "content":"you are content creation sero manager of google, give me a unique name for my youtube channel in which i will do podcasts"
}
message={
    "role": role,
    "content": prompt
}
messages= [message_system, message]
response= clinet.chat.completions.create(model=model, messages=messages, temperature=3)
# print(response)

print("************************************************************************************************")
print(response.choices[0].message.content)