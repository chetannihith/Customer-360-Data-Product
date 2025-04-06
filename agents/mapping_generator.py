import ollama
import yaml

class MappingGenerator:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self, source_info, data_product_structure):
        response = ollama.chat(model=self.model_name, messages=[
            {"role": "system", "content": "You are an expert in creating attribute mappings. Output in YAML format with mappings (source_system, source_attribute, target_table, target_attribute, mapping_type)."},
            {"role": "user", "content": f"Generate mappings from source: {source_info} to target: {data_product_structure}"}
        ])
        yaml_output = response['message']['content']
        try:
            parsed = yaml.safe_load(yaml_output)
            return yaml.dump(parsed, default_flow_style=False)
        except yaml.YAMLError:
            return yaml_output