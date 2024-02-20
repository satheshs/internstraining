st=input()
l=list(st.split(" "))
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)
