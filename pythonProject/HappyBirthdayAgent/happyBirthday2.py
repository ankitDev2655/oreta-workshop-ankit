import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version=api_version
)

print("🎉 Happy Birthday Email Agent Ready!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Goodbye! 🎂")
        break

    # Ask for missing details
    name = input("Agent: What is the person's name? ").strip()
    relationship = input("Agent: What is your relationship (manager, friend, colleague)? ").strip()
    tone = input("Agent: Should the message be formal or casual? ").strip()

    prompt = f"""
    Create a {tone} birthday email.

    Name: {name}
    Relationship: {relationship}
    Tone: {tone}

    Requirements:
    - Include subject line
    - Warm message
    - Professional formatting
    """

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a birthday email generator."},
            {"role": "user", "content": prompt}
        ]
    )

    print("\nAgent:\n" + response.choices[0].message.content + "\n")
