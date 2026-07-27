g="computer"

vowels=0
consonants=0
for i in g:
    i=i.lower()
    if i.isalpha():
        if i in "aeiou":
            vowels+=1
        else:
            consonants+=1
            
print("Vowels:", vowels)
print("Consonants:", consonants)