a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a>=b and a>=c:
    print(f"{a} la so lon nhat")
elif b>=a and b>=c:
    print(f"{b} la so lon nhat")
elif c>=a and c>=b:
    print(f"{c} la so lon nhat")
else:
    print('khong co so nao lon nhat')

