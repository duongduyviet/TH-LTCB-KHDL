while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n > 0:
        break
    print("nhập lại")
S4 = 0
i = 1
while i <= n:
    S4 = S4 + i ** 2
    i = i + 1
print(f"Tổng S4 = {S4}")
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2  
print(f"Tổng S5 = {S5}")

S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2 
print(f"Tổng S6 = {S6}")
