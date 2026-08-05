gt="imcodinginpython"

for i in range(len(gt)):
    for j in range(i+1,len(gt)):
        if gt[i] == gt[j]:
            print(gt[i], end=" ")