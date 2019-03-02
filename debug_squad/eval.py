import json

with open('dev-v2.0.json') as f:
    data = json.load(f)

g = open("dev-2.0-cleaned.txt", "w")


data = data['data']
for y in data:
    questions =y['paragraphs']
    for q in questions:
        qas = q['qas']
        for a in qas:
            answers = a['answers']
            g.write(str(answers) + '\n')