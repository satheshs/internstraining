#1.write the program that takes any word as input and write the letter count.

a="HELLO WORLD"
print('H-',a.count('H'))
print('E-',a.count('E'))
print('L-',a.count('L'))
print('O-',a.count('O'))
print('W-',a.count('W'))
print('R-',a.count('R'))
print('D-',a.count('D'))

#2.Remove Duplicates in a string
b="One Two Three One Four"
words = []
c = b.split()
for i in c:
    if i not in words:
        words.append(i)
print(" ".join(words))

#3.Program that accepts string as input and prints in alternating upper and lower case.

a="python"
b=""
for i in a:
    c=a.index(i)
    if(c % 2==0):
        b+=i.upper();
    else:
        b+=i.lower();
print(b)

#4.Count Capital letters in the given word

a="Python Programming Language"
count=0
for i in a:
    if(i.isupper()):
        count +=1
print(count)

#5.Program that takes string as input and reverse each word of it.

word="Once in a blue moon "
b=[]
c=word.split()
for i in c:
    b.append(i[::-1])
print(" ".join(b))


