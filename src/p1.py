import requests
from openai import OpenAI


print(requests.get("http://localhost:11434").content)

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

response = ollama.chat.completions.create(
    model='llama3.2',
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact"
        }
    ]
)
print(response.choices[0].message.content)

response = ollama.chat.completions.create(
    model='deepseek-r1:1.5b',
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact"
        }
    ]
)
print(response.choices[0].message.content)

