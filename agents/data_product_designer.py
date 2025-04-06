import ollama
import yaml

class DataProductDesigner:
    def __init__(self, model_name):
        self.model_name = model_name

    def design(self, requirements):
        response = ollama.chat(model=self.model_name, messages=[
            {"role": "system", "content": "You are an expert in designing data products for retail banking. Output the structure in YAML format with tables and attributes (name, type)."},
            {"role": "user", "content": f"Design a data product structure based on: {requirements}"}
        ])
        yaml_output = response['message']['content']
        try:
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except yaml.YAMLError:
            return yaml_output  # Fallback to raw output