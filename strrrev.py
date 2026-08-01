tg="he is playing"
res=""
words= tg.split()
for word in words:
    res += word[::-1] + " "

print(res)