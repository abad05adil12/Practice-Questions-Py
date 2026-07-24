f="programming"
vis=""

for ch in f:
    if ch not in vis:
        count=0
        
        for x in f:
            if ch==x:
                count+=1
                
        if count>1:
            print(ch,"=" ,count)
            print(f)
            
        vis+=ch