import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

Q= "what is 22 +33?"

class GPT:
    def __init__(self):
        self.url = os.environ.get('MODEL_URL')
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('HUGGINFACE_INFERENCE_TOKEN')}"}
        self.payload = {
            "inputs": "",
            "parameters": {
                "return_full_text": False,
                "use_cache": True,
                "max_new_tokens": 25
            }

        }

    def query(self, input: str) -> list:
        self.payload["inputs"] = input
        data = json.dumps(self.payload)
        response = requests.request(
            "POST", self.url, headers=self.headers, data=data)
        print(json.loads(response.content.decode("utf-8")))
        return json.loads(response.content.decode("utf-8"))

if __name__ == "__main__":
    #GPT().query("Will artificial intelligence help humanity conquer the universe?")
    #GPT().query("What is the world population?")
    #GPT().query("What is the speed of the fastest computer in the world?")
    #GPT().query("Who is richest man in the world?")
    #GPT().query("Is Elon Musk Alien?")
    #GPT().query("is it possible to hack wifi?")
    GPT().query(Q)
