from pandas import read_csv
import numpy as np
import random
import os

# Check if the file exists before attempting to read it
file_path = "2grams_english.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"No such file or directory: '{file_path}'")

data2 = np.array(read_csv(file_path))

newdata = []
for i in range(len(data2)):
    newdata.append([data2[i][0].split(' ')[0], data2[i][0].split(' ')[1], data2[i][1]])

sorted_three_words = sorted(newdata, key=lambda x: x[0])

wordmap = dict()
for key in sorted_three_words:
    if key[0] not in wordmap:
        wordmap[key[0]] = key[2]
    else:
        wordmap[key[0]] += key[2]

for elem in sorted_three_words:
    elem[2] = elem[2] / wordmap[elem[0]]

def guessWord(initialWord):
    population = []
    pdensity = []
    found = False
    for i in range(len(sorted_three_words)):
        if sorted_three_words[i][0] == initialWord:
            found = True
            population.append(sorted_three_words[i][1])
            pdensity.append(sorted_three_words[i][2])
        elif sorted_three_words[i][0] != initialWord and found:
            break
    return random.choices(population=population, weights=pdensity, k=1)

initialWord = input("Enter the initial word: ")
for i in range(100):
    try:
        initialWord = guessWord(initialWord)[0]
        print(initialWord)
    except IndexError:
        print("No further words found.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break