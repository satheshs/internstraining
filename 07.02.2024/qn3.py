
def solve(st):
    res=""
    for i in range(len(st)):
        if i%2==0:
            res+=st[i].upper()
        else:
            res+=st[i].lower()
    return res
            
st=input()
print(solve(st))
