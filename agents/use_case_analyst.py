import requests

class UseCaseAnalyst:
    def __init__(self, ollama_url):
        self.ollama_url = ollama_url

    def analyze(self, use_case):
        payload = {
            "model": "phi3:mini",
            "messages": [
                {"role": "system", "content": "You are an expert in analyzing business use cases for data products. Provide a concise summary of key requirements."},
                {"role": "user", "content": f"Extract key requirements from this use case: {use_case}"}
            ]
        }
        response = requests.post(self.ollama_url, json=payload)
        return response.json()["message"]["content"]