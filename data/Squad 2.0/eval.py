import json
import re

def writeCleanTrainJson():
    with open('train-v2.0.json') as f:
        data = json.load(f)

    g = open("train-2.0-cleaned.txt", "w")


    data = data['data']
    for y in data:
        questions =y['paragraphs']
        for q in questions:
            qas = q['qas']
            for a in qas:
                answers = a['answers']
                answers = [a['text'].encode('utf-8') for a in answers]
                answers = str([a for a in answers]).strip('[]')

                g.write(answers + '\n')

def writeCleanDevContextsJson():
    with open('dev-v2.0.json') as f:
        data = json.load(f)
    g = open("dev-2.0-cleaned_contexts.txt", "w")
    data = data['data']
    for y in data:
        questions =y['paragraphs']
        for q in questions:
            context = q['context']
            g.write(str(context.encode('utf-8')) + '\n')

import json
def writeCleanDevQuestionsJson():
    with open('dev-v2.0.json') as f:
        data = json.load(f)
    g = open("dev-2.0-cleaned_questions.txt", "w")
    data = data['data']
    for y in data:
        questions =y['paragraphs']
        for q in questions:
            qas = q['qas']
            for a in qas:
                question = a['question']
                g.write(str(question.encode('utf-8')) + '\n')


def parseResults(filepath):
    data = None
    with open('train-2.0-cleaned.txt') as f:
        data = f.readlines()
        data = [d.split(",") for d in data]
        for i in range(len(data)):
            data[i] = [re.sub('\"|\'', '', a).strip() for a in data[i]]

    return data

def AScore(filepath):
    data = parseResults(filepath)
    totalNum = len(data)
    numNA = 0.0
    for i in range(len(data)):
        if data[i] == [""]:
            numNA +=1

    return 1 - numNA / totalNum

# writeCleanDevQuestionsJson()
# jsonToCSV()
# writeCleanDevJson()
filepath = "../debug_squad_WHL/dev_submission.csv"

writeCleanTrainJson()
print("Percent of Total Contexts that have Answers: " + str(AScore(filepath)))