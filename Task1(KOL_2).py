# 1) x dəyişəni
x = 5
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2) n rəqəmi
n = 4
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

# 3) a, b, c rəqəmləri
a, b, c = 5, 9, 2
print(max(a, b, c))

# 4) day dəyişəni
day = 3
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(days.get(day, "Yanlış gün"))

# 5) temp dəyişəni
temp = 15
if temp < 0:
    print("soyuq")
elif temp <= 20:
    print("normal")
else:
    print("isti")

# 6) password stringi
password = "mypassword123"
length = len(password)
if length < 8:
    print("qısa")
elif 8 <= length <= 12:
    print("orta")
else:
    print("uzun")

# 7) x rəqəmi 3 və 5-ə bölünmə
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8) 0-dan 20-yə qədər cüt rəqəmlər
for i in range(0, 21):
    if i % 2 == 0:
        print(i)

# 9) "Bağda ərik var idi …" hərf-hərf çap
text = "Bağda ərik var idi …"
for char in text:
    print(char)

# 10) 1-dən 10-a qədər 3 xaric
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11) 1-dən başlayaraq ilk 5-ə bölünən rəqəmi tap
i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

# 12) (1, 3, 5, 7, 9) içində 5-in indeksini tap
nums = (1, 3, 5, 7, 9)
for index, num in enumerate(nums):
    if num == 5:
        print(index)
        break
