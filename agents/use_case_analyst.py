import ollama

class UseCaseAnalyst:
    def __init__(self, model_name):
        self.model_name = model_name

    def analyze(self, use_case):
        response = ollama.chat(model=self.model_name, messages=[
            {"role": "system", "content": "You are an expert in analyzing business use cases for data products. Provide a concise summary of key requirements."},
            {"role": "user", "content": f"Extract key requirements from this use case: {use_case}"}
        ])
        return response['message']['content']