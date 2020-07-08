string = "Hello World Here"
x = string.split()
y = []
b = 1
while b <= len(x):    
    y.append(x[len(x) - b])
    b += 1
print(*y)
