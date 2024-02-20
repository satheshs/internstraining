#1.a=input("Enter a word:")
  d=set()
  for i in a:
    if i not in d and i!='-':
       print(i,"-",a.count(i))
       d.add(i)

#2.a=input("Enter the words:")
  d=set()
  b=a.split()
  for i in b:
      if i not in d:
        print(i, end=" ")
        d.add(i)

#3.t="python"
   b=0
   for i in t:
    if(b%2==0):
      print(i.upper(), end="")
      b+=1
    else:
      print(i, end="")
      b+=1

#4.txt="SuRuThI"
   count=0
   for i in txt:
     if(i.isupper()):
      count+=1
   print("The capital letter are:",count)

#5.t="Once in a blue Moon"
   a=t.split()
   for i in a:
     n=i[::-1]
     print(n, end=" ")



