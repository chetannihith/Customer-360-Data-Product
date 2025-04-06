import ollama
import yaml

class SourceIdentifier:
    def __init__(self, model_name):
        self.model_name = model_name

    def identify(self, data_product_structure):
        response = ollama.chat(model=self.model_name, messages=[
            {"role": "system", "content": "You are an expert in identifying source systems for data products. Output in YAML format with systems and attributes (name, description)."},
            {"role": "user", "content": f"Identify source systems and attributes for this data product structure: {data_product_structure}"}
        ])
        yaml_output = response['message']['content']
        try:
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except yaml.YAMLError:
            return yaml_output