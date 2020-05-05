import requests
import json

questions = set()

while True:
    r = requests.get('https://secure.jfs.ohio.gov/jfsQACaptchaForEktronService.asmx/GetNewQuestion')
    question = json.loads(r.json()['d'])['Question']
    if question not in questions:
        questions.add(question)

        with open('questions.json', 'w+') as f:
            arr = sorted(list(questions))
            json.dump(arr, f, indent=4)

    print(len(questions))
