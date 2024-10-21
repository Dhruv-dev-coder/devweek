from together import Together
from together.resources.chat import completions

client = Together(
    api_key="5a6ce137fb4b048a950322cc102fc58b7288952c5ee8c63b418f19c5731bfcb6")


def start():
    History = []

    messages = input("How can I help you today?:")
    if messages == "quit":
      return
        

    History.append({"role": "userInput", "content": messages})

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{
            "role": "userInput",
            "content": messages
        }])
    answer = completion.choices[0].message.content
    print("Together ai:- ", answer)
    History.append({"role": "assistant", "content": answer})
    start()




start()
print("done")