import sys
import re

def parse(consent: str):
    pass

for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    try:
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
                    if '^'+match.group(1) in content[j]:
                        content.insert(k, content[j])
                        answerInx = j
                        break

        for k in range(len(content)):
            if '^' in content[k]:
                del content[k]

    except:
        continue