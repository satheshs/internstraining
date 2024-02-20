numbers=(10,20,30,40,50,60,70,80,90)
print(numbers[1])

print(numbers[-1:-4:-1])



marks=(120,340,789,74,48)
tot=numbers+marks
print(tot[-1:-4:-1])

colors=("red","blue","green")
color1,color2,color3=colors
print(color1)
print(color2)
print(color3)





import math
point=(3,4)
origin=(0,0)
x=point[0]-origin[0]
y=point[1]-origin[1]
distance=math.sqrt(x**2+y**2)
print(distance)
