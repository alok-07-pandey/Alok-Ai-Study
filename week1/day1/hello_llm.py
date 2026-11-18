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
role="user"
prompt="Do you know Alok speaks youtube channel who. do podcast "
message={
    "role": role,
    "content": prompt
}
messages= [message]
response= clinet.chat.completions.create(model=model, messages=messages)
print(response)

print("************************************************************************************************")
print(response.choices[0].message.content)