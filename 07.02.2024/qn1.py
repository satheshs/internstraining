st=input()
res=[" "]
for i in range(len(st)):
    if st[i] not in res:
        res.append(st[i])
        print(st[i],"- ", st.count(st[i]))
