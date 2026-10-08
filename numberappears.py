numbers=[1,1,34,5,3,2,4]

for i in range (len(numbers)):
    count=0
    
    for j in range(len(numbers)):
        if numbers[i]==numbers[j]:
            count+=1
    
    print(numbers[i], "appears", count, "times")