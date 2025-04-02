import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
print(API_KEY)

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_story(prompt):
    """Generate a short story based on user input."""
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.json()}"

if __name__ == "__main__":
    user_prompt = input("Enter a story prompt: ")
    story = generate_story(user_prompt)
    print("\nGenerated Story:\n", story)
