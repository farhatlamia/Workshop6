import csv
import numpy as np
import pandas as pd

f = open("buggy-python.txt", "r")
Lines = f.readlines()
Word = []
Time = {}

a = open("neutral-python.txt", "r")
Lines1 = a.readlines()
Word1 = []
Time1 = {}

print("buggy-python.txt")
for line in Lines:
    command = line.split(" ")[1].split("(")[0]
    command1 = line.split(" ")[-1].split(">")[0].split("<")[-1]
    #print(command1)
    Word.append(command)
    Time.update({command:command1})
print(Time)
#print(Word)
uniqWords = sorted(set(Word))
for word in uniqWords:
    print(word, Word.count(word))
    
print("neutral-python.txt")
for line in Lines1:
    command = line.split(" ")[1].split("(")[0]
    command1 = line.split(" ")[-1].split(">")[0].split("<")[-1]
    Word1.append(command)
    Time1.update({command:command1})
#print(Word1)
print(Time1)
uniqWords = sorted(set(Word1))
for word in uniqWords:
    print(word, Word1.count(word))

#np.savetxt('buggy-python.csv', [p for p in zip(Time)], delimiter=',', fmt='%s')
#np.savetxt('neutral-python.csv', [p for p in zip(Time1)], delimiter=',', fmt='%s')
a_file = open("buggy-python.csv", "w")
writer = csv.writer(a_file)
for key, value in Time.items():
    writer.writerow([key, value])

a_file.close()

b_file = open("neutral-python.csv", "w")
writer = csv.writer(b_file)
for key, value in Time1.items():
    writer.writerow([key, value])

b_file.close()


