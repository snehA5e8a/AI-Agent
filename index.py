from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('HF_API_TOKEN')
client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2",
            token=api_token
        )
prompt = '''role: "user",
        content: "Give me a list of activity ideas based on my current location and weather"
        '''
response = client.text_generation(
                prompt,
                max_new_tokens=180,
                temperature=0.6,  # randomness from consistency to creativity (RFL)
                repetition_penalty=1.2, # Small penalty
                return_full_text=False # No need of returning prompt 
            )
print(response)
