import os 
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

messages = []

while True:
    user_prompt = input('User: ')
    messages.append(
        {'role': 'user', 'content': user_prompt}
    )

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    chat_completion = client.chat.complitions.create(
        messages=messages,
        model = "gpt-4"
    )

    response_text = chat_completion.choices[0].messages.content 

    print(response_text)