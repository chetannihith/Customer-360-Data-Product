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
        response = requests.post(self.ollama_url, json=payload)
        try:
            yaml_output = response.json()["message"]["content"]
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except (requests.JSONDecodeError, KeyError, yaml.YAMLError):
            return response.text  # Fallback to raw text