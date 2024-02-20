def solve(st):
    open=['(','{','[']
    temp=[]
    for i in st:
        if i in open:
            temp.append(i)
        elif len(temp)>0:
            if i==']' and temp[-1]=='[':
                temp.pop()
            elif i=='}' and temp[-1]=='{':
                temp.pop()
            elif i==')' and temp[-1]=='(':
                temp.pop()
        else:
            return False
    if len(temp)>0:
        return False
    else:
        return True
st=input()
print(solve(st))