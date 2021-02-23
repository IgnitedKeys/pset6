from cs50 import get_string

text = get_string("Enter Text:\n")

#0.0588 * L - 0.296 * S - 15.8   L= avg num of letter per 100 words S= avg num of sentences per 100 words

letters = 0
words = 1
sentences = 0


for i in range(len(text)):
    if(str.isalpha(text[i]) == True):
        letters += 1
        
    elif(str.isspace(text[i]) == True):
        words += 1
       
    elif(text[i] == "." or text[i] == "!" or  text[i] == "?"):
        sentences += 1
l = letters /words * 100
s = sentences / words * 100

index = round(0.0588 * l - 0.296 * s - 15.8)
#print(f"{index}")
grade = index

if(grade >= 1 and grade <= 16):
    print(f"Grade {grade}")
elif(grade < 1):
    print("Before Grade 1")
elif(grade > 16):
    print("Grade 16+")
    