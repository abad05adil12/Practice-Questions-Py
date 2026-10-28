word = "programming"
checked = ""

for i in range(len(word)):
    count = 0

    for j in range(len(word)):
        if word[i] == word[j]:
            count += 1

    if count == 2 and word[i] not in checked:
        print(word[i])
        checked += word[i]