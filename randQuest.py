import re
import random

with open('report.txt', 'rb') as file:
    content = file.read().decode('utf-8').split('\n')
    questionIndexes = []
    for i in range(len(content)):
        if 'Задание # ' in content[i]:
            questionIndexes.append(i)

index = random.randint(0, len(questionIndexes)-2)
for line in content[questionIndexes[index]:questionIndexes[index+1]]:
    if not 'Верный ответ' in line:
        print(line)
    else:
        answer = line

input("Press enter to show the answer.")
print(answer)
