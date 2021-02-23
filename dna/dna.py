import sys
import csv
from csv import DictReader, reader

#command line arg check
if len(sys.argv) != 3:
    sys.exit("missing command-line argument")

#open dna sequence and store it as a string
with open(sys.argv[2], "r") as dna_file:
    dna = dna_file.read()

#print(f"{dna}")

sequences = {}

#open csv and read into a list
with open(sys.argv[1], "r") as csv_file:
    people = reader(csv_file)
    for row in people:
        csv_dna = row
        csv_dna.pop(0)
        break
#copy list into dictionary
for n in csv_dna:
    sequences[n] = 0

#print(f"{sequences}")


#compute longest run of consecutive repeats in DNA
for key in sequences:
    #len of key in dic
    k = len(key)
    tmp_max = 0
    tmp = 0
    for i in range(len(dna)):
        #resets tmp counter
        while tmp > 0:
            tmp -= 1
       
        if dna[i:i+k] == key:
            #add 1 to first match
            if tmp == 0:
                tmp += 1
            #added to tmp after each repeat
            while dna[i - k:i] == dna[i:i+k]:
                tmp += 1
                i += k
            #updates the max 
            if tmp > tmp_max:
                tmp_max = tmp
    #add max value to dictionary value
    sequences[key] += tmp_max
#print(f"{sequences}")
    
#compare dna counts to person or no match

#open csv and add names into dictionary
with open(sys.argv[1]) as csv_file:
    people = DictReader(csv_file)
    for person in people:
        counter = 0
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                counter += 1
        if counter == len(sequences):  #check the len(sequences)
            print(f"{person['name']}")
            sys.exit()
    print("no match")
        
            
    
    
    
       
        