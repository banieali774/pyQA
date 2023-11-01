from qa_model import QAModel

def main():
    data_file = 'sample_data.json'
    model = QAModel(data_file)

    print("Welcome to the Python Q&A system!")
    print("Type 'quit' to exit.")

    while True:
        question = input("\nEnter your question: ")
        if question.lower() == 'quit':
            break

        answer = model.find_answer(question)
        print("Answer:", answer)

if __name__ == '__main__':
    main()
