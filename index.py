from huggingface_hub import InferenceClient
import os
import asyncio
import yaml
from dotenv import load_dotenv
from tools import getCurrentWeather, getLocation

load_dotenv()

api_token = os.getenv('HF_API_TOKEN')
client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2",
            token=api_token
        )


with open('prompts.yaml', 'r') as file:
    SYSTEM_MESSAGES = yaml.safe_load(file)

async def agent(query):
        message = [
                {'role': 'system', 'content':SYSTEM_MESSAGES['system_prompt']},
                {'role': 'user', 'content': query},
                ]
        response = client.chat_completion(
                message,
                temperature=0.6,  # randomness from consistency to creativity (RFL)
        )
        print(response['choices'][0]['message']['content'])

async def main():
    await agent("What should I read today??")

# Run the async code
if __name__ == "__main__":
    asyncio.run(main())

