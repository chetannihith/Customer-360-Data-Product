import requests
import yaml

class MappingGenerator:
    def __init__(self, ollama_url):
        self.ollama_url = ollama_url

    def generate(self, source_info, data_product_structure):
        payload = {
            "model": "phi3:mini",
            "messages": [
                {"role": "system", "content": "You are an expert in creating attribute mappings. Output in YAML format with mappings (source_system, source_attribute, target_table, target_attribute, mapping_type)."},
                {"role": "user", "content": f"Generate mappings from source: {source_info} to target: {data_product_structure}"}
            ]
        }
        response = requests.post(self.ollama_url, json=payload)
        try:
            yaml_output = response.json()["message"]["content"]
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except (requests.JSONDecodeError, KeyError, yaml.YAMLError):
            return response.text  # Fallback to raw text