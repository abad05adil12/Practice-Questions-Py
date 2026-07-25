vfx="abba"
palindrome=True
for i in range(len(vfx)//2):
    if vfx[i]!=vfx[len(vfx)-i-1]:
        palindrome=False
        break
    
if palindrome:
    print("\npalindrome")
else:
    print("\nnot palindrome")