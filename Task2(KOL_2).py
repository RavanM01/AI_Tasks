# 1) salam funksiyası
def salam():
    print("Salam, Dünya!")

# 2) kub_hesabla funksiyası
def kub_hesabla(n):
    return n ** 3

# 3) birlesdir funksiyası
def birlesdir(soz1, soz2):
    return soz1 + " " + soz2

# 4) cap_et funksiyası
def cap_et(liste):
    for element in liste:
        print(element)

# 5) toplam funksiyası
def toplam(*args):
    return sum(args)

# 6) ortalama funksiyası
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7) adlar_rəqəmlər funksiyası
def adlar_reqemler(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")

# 8) tip_yoxla funksiyası
def tip_yoxla(deyer):
    if isinstance(deyer, str):
        print("mətn")
    elif isinstance(deyer, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

# 9) yas_kateqoriya funksiyası
def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

# 10) soz_uzunluq funksiyası
def soz_uzunluq():
    soz = input("Bir söz daxil edin: ")
    print(len(soz))
