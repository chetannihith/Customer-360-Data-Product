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