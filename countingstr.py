pl="success"
result={}

for i in pl:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
        
for key, value in result.items():
    print(key, "=", value)
    