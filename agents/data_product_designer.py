import requests
import yaml

class DataProductDesigner:
    def __init__(self, ollama_url):
        self.ollama_url = ollama_url

    def design(self, requirements):
        payload = {
            "model": "phi3:mini",
            "messages": [
                {"role": "system", "content": "You are an expert in designing data products for retail banking. Output the structure in YAML format with tables and attributes (name, type)."},
                {"role": "user", "content": f"Design a data product structure based on: {requirements}"}
            ]
        }
        response = requests.post(self.ollama_url, json=payload)
        try:
            yaml_output = response.json()["message"]["content"]
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except (requests.JSONDecodeError, KeyError, yaml.YAMLError):
            return response.text  # Fallback to raw text