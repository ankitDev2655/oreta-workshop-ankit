import os
from openai import AzureOpenAI
from dotenv import load_dotenv


endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = "gpt-4o-mini"
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

print("Chatbot started! Type 'exit' to quit.\n")

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break

    # Add user input to history
    conversation_history.append({"role": "user", "content": user_input})

    # Send to Azure OpenAI
    response = client.chat.completions.create(
        messages=conversation_history,
        model=deployment,
        max_tokens=4096,
        temperature=1.0
    )

    reply = response.choices[0].message.content

    # Print assistant reply
    print("Assistant:", reply)

    # Add reply to conversation history
    conversation_history.append({"role": "assistant", "content": reply})
