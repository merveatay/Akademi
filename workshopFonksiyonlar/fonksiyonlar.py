def fib():
    a = 1
    b = 0
    c = 0
    list = []
    while len(list)<20:
        c = a+b
        a = b
        b = c
        list.append(b)
    print(list)
fib();

def perfect():
    toplam = 0
    sayi = int(input("Sayı giriniz: "))
    for i in range(1,sayi):
        if sayi%i == 0:
            toplam += i
    if toplam == sayi:
        print("Mükemmel sayı")
    else:
        print("Mükemmel sayı değil")
perfect();

def enBuyuk():
    nums = []
    for i in range(10):
        num = int(input("Sayı girin:"))
        nums.append(num)
    enBuyuk = max(nums)
    x = f"En büyük değer: {enBuyuk}"
    print(x)
enBuyuk();

def ustLimit():
    numList = []
    ustLimit = int(input("Üst limit giriniz: "))
    altLimit = int(input("Alt limit giriniz: "))
    for i in range(altLimit+1, ustLimit):
        if i%2 == 0 and i > 0:
            numList.append(i)
    print(numList)
ustLimit();





