by="pakistan"
visited=""
min_count=len(by)+1
min_chr=""

for ch in by:
    if ch not in visited:
        count=0
        for x in by:
            if ch==x:
                count+=1
                
            if count<min_count:
               min_count=count
               min_chr=ch
            visited+=ch
            
print(min_chr)