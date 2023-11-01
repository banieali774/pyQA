import json

class QAModel:
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    def load_data(self, data_file):
        with open(data_file, 'r') as file:
            data = json.load(file)
        return data

    def find_answer(self, question):
        for item in self.data:
            if item['question'].lower() == question.lower():
                return item['answer']
        return "Sorry, I don't have an answer for that question."
