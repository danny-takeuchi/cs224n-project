import json
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
                g.write(str(answers) + '\n')


def jsonToCSV():
    import csv
    # Write submission file for Kaggle
    with open('dev_submission.csv', 'w') as csv_fh:
        csv_writer = csv.writer(csv_fh, delimiter=',')
        csv_writer.writerow(['Id', 'Predicted'])

        with open('predictions.json') as f:
            data = json.load(f)
            for uuid in data:
                csv_writer.writerow([uuid, data[uuid]])

jsonToCSV()