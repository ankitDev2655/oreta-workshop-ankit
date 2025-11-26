import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = "2024-12-01-preview"  # Working version for Azure

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version=api_version
)

SYSTEM_PROMPT = """
You are a Happy Birthday Email Agent.
Your only job is to write warm, friendly, and professional birthday emails.
Rules:
- Always respond in an email format (Subject + Body).
- Keep tone friendly and respectful.
- If user asks something not related to birthdays, answer:
  "I can only create birthday emails."
- Ask for the person's name if not provided.
"""

print("🎉 Happy Birthday Email Agent Ready!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Goodbye! 🎂")
        break

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        max_tokens=1000,
        temperature=0.5
    )

    print("\nAgent:\n" + response.choices[0].message.content + "\n")
