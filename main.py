import random

c = 101
x = random.randint(1,100)
can = int(input("kaç hak kullanmak istersiniz? "))
hak = can
sayac = 0
while hak > 0:
    c = int(input("tahmin: "))
    hak -= 1
    sayac += 1
    if c < x:
        print("yukarı")
    elif c > x:
        print("aşağı")
    elif c == x:
        print(f"{sayac}. defada bildiniz. tebrikler! toplam puanınız: {100-(100/can) * (sayac-1)}")
        break
    if hak == 0:
        print("bilemediniz!")
        print(f"cevap {x} idi.")
        break
    print(f"kalan hakkınız: {hak}")