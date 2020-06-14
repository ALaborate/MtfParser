import sys
import re


def parse(consent: str):
    pass


for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    # try:
    with open(filename, 'rb') as file:
        content = file.read().decode('utf-8').split('\n')
    taskChecker = re.compile(r'Задание # (\d{1,3})')
    answerChecker = re.compile(r'\^\d{1,3}')
    answerInx = 0
    for j in range(len(content)):
        match = answerChecker.search(content[j])
        if match:
            answerInx = j
            break

    for k in range(len(content)):
        match = taskChecker.search(content[k])
        if match:
            for j in range(answerInx, len(content)):
                numb = '^'+match.group(1)
                if numb in content[j]:
                    answer = content[j].replace(numb+') ', '')
                    content.insert(k+1, answer)
                    answerInx = j
                    break
    k = 0
    while k < len(content):
        if '^' in content[k]:
            del content[k]
        k += 1

    with open('report.txt', 'wb') as file:
        data = '\n'.join(content).encode('utf-8')
        file.write(data)
