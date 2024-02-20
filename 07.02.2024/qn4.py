st=input()
count=0
for i in range(len(st)):
    if st[i].isupper():
        count+=1
print(count)
