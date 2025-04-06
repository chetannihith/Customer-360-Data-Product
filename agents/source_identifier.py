import requests
import yaml

class SourceIdentifier:
    def __init__(self, ollama_url):
        self.ollama_url = ollama_url

    def identify(self, data_product_structure):
        payload = {
            "model": "phi3:mini",
            "messages": [
                {"role": "system", "content": "You are an expert in identifying source systems for data products. Output in YAML format with systems and attributes (name, description)."},
                {"role": "user", "content": f"Identify source systems and attributes for this data product structure: {data_product_structure}"}
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
        if full_content:
            try:
                parsed = yaml.safe_load(full_content)
                return yaml.dump(parsed, default_flow_style=False)
            except yaml.YAMLError:
                return full_content
        return response.text