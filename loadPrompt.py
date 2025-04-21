import json

def load_react_prompt():
    with open('react_prompt.txt', 'r') as f:
        prompt = json.load(f)
    return prompt

prompt = load_react_prompt()
print(prompt)