f = open("buggy-python.txt", "r")
Lines = f.readlines()
Word = []
Words = []

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
#print(Word)
Words = unique(Word)
print(Words)

    


    


