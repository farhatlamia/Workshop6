f = open("buggy-python.txt", "r")
a = open("neutral-python.txt", "r")
Lines = f.readlines()
Lines1 = a.readlines()
Word = []
Words = []
name  = []
Name = []

print("buggy-python.txt")
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)
        
for line in Lines:
    command = line.split(" ")[1].split("(")[0]
    #print(command)
    Word.append(command)
    occurrences = Word.count(command)
    #print(command, occurrences)
#print(Word)
Words = unique(Word)
#print(Words)

print("neutral-python.txt")
for i in Lines1:
    command1 = i.split(" ")[1].split("(")[0]
    #print(command)
    name.append(command1)
    occurrences = name.count(command1)
    #print(command1, occurrences)
#print(Word)
Name = unique(name)
#print(Name)


    


