a = []
for i in range (10):
    a.append(i)
print(a)

b = [i for i in range(10)]
print(b)

for i in range(10):
    if (1 % 2) == 0:
        print("짝수")
        
c = [i for i in range(10) if 1 % 2 == 0]