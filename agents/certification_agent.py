import requests

class CertificationAgent:
    def __init__(self, ollama_url):
        self.ollama_url = ollama_url

    def certify(self, data_product_structure):
        payload = {
            "model": "phi3:mini",
            "messages": [
                {"role": "system", "content": "You are an expert in certifying data products. Provide ingress, egress, and certification details in plain text."},
                {"role": "user", "content": f"Define ingress, egress, and certification details for: {data_product_structure}"}
            ]
        }
        response = requests.post(self.ollama_url, json=payload)
        return response.json()["message"]["content"]