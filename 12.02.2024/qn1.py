
def solve(l):
    tot=0
    for i in range(len(l)):
        tot+=l[i]*l[i]
    return tot


l=list(map(int,input("Enter the list of numbers: ").split()))
print(solve(l))
