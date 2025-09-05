# Aufgabe 4 Struktogramme

#a)
print('Hello World')

#b)
s = 0
for i in range(1, 101):
    s += i
print(s)

#c)
i = 1
while i <= 100:
    print(i)
    i = i + 1
    if i == 39:
        i = 61

#d)
def Quadratzahlen(n):
    i = 1
    q = 1
    while q <= n:
        i += 1
        print(q)
        q = i * i
Quadratzahlen(10)


