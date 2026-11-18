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
# 3 prompts 
prompt1="Hii"
prompt2="Explain me ai engineering"
prompt3="write essay on enginnering in 1000 words"

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role": role,
        "content": prompt
    }
    messages= [message]
    response=clinet.chat.completions.create(model=model, messages=messages, max_tokens=50)
    usage=response.usage

    print("************************************************************************************************")
    print(f"Prompt: {prompt} --> your token: {usage.prompt_tokens} completion_token: {usage.completion_tokens} total_tokens: {usage.total_tokens} Finish_reason: {response.choices[0].finish_reason}")
