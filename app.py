# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import os

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
if DEEPSEEK_API_KEY is None:
    raise ValueError("Please set the DEEPSEEK_API_KEY environment variable")

client = OpenAI(base_url="https://api.deepseek.com", api_key=DEEPSEEK_API_KEY)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
)

print(response.choices[0].message.content)
