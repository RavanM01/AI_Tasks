# 1
reqemler = [5, 10, 15, 20]

# 2
print("Uzunluq:", len(reqemler))

# 3
reqemler.append(25)
print("25 əlavə olundu:", reqemler)

# 4
reqemler.insert(2, 12)
print("2-ci indeksə 12 əlavə olundu:", reqemler)

# 5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis = list1 + list2
print("Birləşmiş list:", birlesmis)

# 6
print("2-ci və 3-cü elementlər:", reqemler[2:4])

# 7
reqemler[0] = 50
print("İlk element 50 ilə əvəz olundu:", reqemler)

# 8
print("19 listdədir?", 19 in reqemler)

# 9
hərfler = ["a", "b", "a", "c"]
print("'a' neçə dəfə var:", hərfler.count("a"))

# 10
simvollar = ["x", "y", "x", "z"]
simvollar = [i for i in simvollar if i != "x"]
print("'x'siz list:", simvollar)

# 11
siyahi = [7, 2, 9, 1]
siyahi.sort(reverse=True)
print("Azalan sıra:", siyahi)

# 12
boyukler = [i for i in reqemler if i > 10]
print("10-dan böyük elementlər:", boyukler)