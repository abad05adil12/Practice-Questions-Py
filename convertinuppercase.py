st="python"
res=""
for i in st:
    if 'a'<='i'<='z':
        print(i,end="")
        
        res+=chr(ord(i)-32)
    else:
        res+=i
        
print("\n Uppercase string: ", res)