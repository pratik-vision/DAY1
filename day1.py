# Q1:swap number
a=1,2,3,2
b=3,4,24,2
a,b=b,a
print(a,b)

# Q2: area of rectangle
len=float(input('enter len='))
bre=float(input('enter bre='))
area=len * bre
print(f"area ={area}")

# Q3: perimeter of rectangle
len=float(input('enter len='))
bre=float(input('enter ber='))
peri=2*(len * bre)
print(f'perimeter={peri}')

# # Q4:simple interest
m=float(input('enter the amount='))
r=float(input('enter rate='))
t=float(input('enter time='))
i=(m * r * t)/100
o=i + m
print(f'profit ={i} total amount={o}')

# Q5: BMI
w=float(input('enter weight='))
h=float(input('enter height='))
o=w /(h * h)
print(f'BMI={o}')

# Q7: square and cube
i=int(input('enter num='))
print("square=",i ** 2)
print("cube=",i ** 3)
