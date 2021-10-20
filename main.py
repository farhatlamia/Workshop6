import csv

f = open("buggy-python.txt", "r")
Lines = f.readlines()
Word = []

a = open("neutral-python.txt", "r")
Lines1 = a.readlines()
Word1 = []

print("buggy-python.txt")
for line in Lines:
    command = line.split(" ")[1].split("(")[0]
    Word.append(command)
#print(Word)
uniqWords = sorted(set(Word))
for word in uniqWords:
    print(word, Word.count(word))
    
print("neutral-python.txt")
for line in Lines1:
    command = line.split(" ")[1].split("(")[0]
    Word1.append(command)
#print(Word1)
uniqWords = sorted(set(Word1))
for word in uniqWords:
    print(word, Word1.count(word))
    


    

    




    


