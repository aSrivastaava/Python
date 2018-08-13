x=int(input("Enter the First Number: "))
y=int(input("Enter the Second Number: "))

if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
        gcd = i

print("GCD = ",gcd)

poxy = 1
for pox in range(1, y+1):
    poxy = poxy*x

print(poxy)

