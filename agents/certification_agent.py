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
        response = requests.post(self.ollama_url, json=payload, stream=True)
        full_content = ""
        for chunk in response.iter_content(chunk_size=1024, decode_unicode=True):
            if chunk:
                try:
                    chunk_str = chunk.decode('utf-8')
                    if '"content":"' in chunk_str:
                        start = chunk_str.index('"content":"') + 11
                        end = chunk_str.index('"', start)
                        full_content += chunk_str[start:end]
                except (ValueError, UnicodeDecodeError):
                    continue
        return full_content if full_content else response.text