import re
import random

with open('report.txt', 'rb') as file:
    content = file.read().decode('utf-8').split('\n')
    questionIndexes = []
    for i in range(len(content)):
        if 'Задание # ' in content[i]:
            questionIndexes.append(i)

index = random.randint(0, len(questionIndexes)-2)
answerChecker = re.compile(r'Верны\w ответ\w?')
for line in content[questionIndexes[index]:questionIndexes[index+1]]:
    match = answerChecker.search(line)
    if match:
        answer = line
    else:
        print(line)

input("Press enter to show the answer.")
print(answer)
