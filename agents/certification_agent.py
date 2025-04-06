import ollama

class CertificationAgent:
    def __init__(self, model_name):
        self.model_name = model_name

    def certify(self, data_product_structure):
        response = ollama.chat(model=self.model_name, messages=[
            {"role": "system", "content": "You are an expert in certifying data products. Provide ingress, egress, and certification details in plain text."},
            {"role": "user", "content": f"Define ingress, egress, and certification details for: {data_product_structure}"}
        ])
        return response['message']['content']