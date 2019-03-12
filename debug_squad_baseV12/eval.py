import json
import re

def writeCleanDevJson():
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
                answers = [a['text'].encode('utf-8') for a in answers]
                answers = str([a for a in answers]).strip('[]')

                g.write(answers + '\n')

import json
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

def jsonToCSV():
    import csv
    # Write submission file for Kaggle
    with open('dev_submission.csv', 'w') as csv_fh:
        csv_writer = csv.writer(csv_fh, delimiter=',')
        csv_writer.writerow(['Id', 'Predicted'])

        with open('predictions.json') as f:
            data = json.load(f)
            for uuid in data:
                csv_writer.writerow([uuid, data[uuid].encode('utf-8')])

def parseResults(filepath):
    data = None
    results = None
    with open('dev-2.0-cleaned.txt') as f:
        data = f.readlines()
        data = [d.split(",") for d in data]
        for i in range(len(data)):
            data[i] = [re.sub('\"|\'', '', a).strip() for a in data[i]]

    with open(filepath) as f:
        results = f.readlines()[1:]
        results = [r.split(",", 1)[1].strip() for r in results]

    return data, results

#getAnsweredNonanswersScore
def ANaScore(filepath):
    data, results = parseResults(filepath)
    numNonAnswers = 0.0
    numAnsweredNonanswers = 0.0
    for i in range(len(data)):
        if data[i] == [""]:
            numNonAnswers +=1
            if results[i] != "":
                numAnsweredNonanswers +=1

    return numAnsweredNonanswers / numNonAnswers

#getNonansweredAnswersScore
def NaAScore(filepath):
    data, results = parseResults(filepath)
    numAnswers = 0.0
    numNonansweredAnswers = 0.0
    for i in range(len(data)):
        if data[i] != [""]:
            numAnswers +=1
            if results[i] == "":
                numNonansweredAnswers +=1

    return numNonansweredAnswers / numAnswers

def AAScore(filepath):
    data, results = parseResults(filepath)
    numAnswers = 0.0
    numWrongAnswers = 0.0
    for i in range(len(data)):
        if data[i] != [""] and results[i] != "":
            numAnswers +=1
            if results[i] not in data[i]:
                numWrongAnswers +=1

    return 1 - numWrongAnswers / numAnswers

# writeCleanDevQuestionsJson()
jsonToCSV()
# writeCleanDevJson()
filepath = "../debug_squad_baseV12/dev_submission.csv"
print("getAnsweredNonanswersScore: " + str(ANaScore(filepath)))
print("getNonansweredAnswersScore: " + str(NaAScore(filepath)))
print("WrongAnswersScore: " + str(AAScore(filepath)))

import matplotlib.pyplot as plt
with open("../debug_squad_baseV12/loss.csv", "r") as f:
    x = f.readlines()
    for i in range(len(x)):
        x[i] = x[i].split(",")
        for j in range(len(x[i])):
            m = re.search("([0-9]\.[0-9]{4})", x[i][j])
            if m:
                x[i][j] = m.group(1)
            else:
                x[i][j] = ""
        x[i] = [j for j in x[i] if j != ""]

def plot(x, y):
    plt.plot(x, y)
    plt.ylabel("Loss")
    plt.xlabel("Iteration")
    plt.show()

plot([i for i in range(len(x[2]))], x[2])