# 1) s1 adlı list yaratmaq
s1 = [10, 20, 30, 40]

# 2) s1-ə 'w', 'x', 'y', 'z' indekslərini təyin etmək
indices = ['w', 'x', 'y', 'z']
s1_dict = dict(zip(indices, s1))
print(s1_dict)

# 3) Python dictionary-dən s2 adlı dictionary yaratmaq
s2 = {'p': 5, 'q': 10, 'r': 15}
print(s2)

# 4) s2-dən 'q' indeksli elementi seçmək
print(s2['q'])

# 5) s1-dən 25-dən böyük elementləri seçmək
print([x for x in s1 if x > 25])

# 6) s1-də 20-dən böyük elementləri 10-a bölmək
print([x / 10 for x in s1 if x > 20])

# 7) ((1, 2), (3, 4)) listindən df1 yaratmaq
df1 = [(1, 2), (3, 4)]
print(df1)

# 8) df1-ə ('r1', 'r2') sətir adlarını təyin etmək
df1_dict = {'r1': (1, 2), 'r2': (3, 4)}
print(df1_dict)

# 9) Python dictionary-dən df2 yaratmaq
df2 = {'A': [1, 2], 'B': [3, 4]}
print(df2)

# 10) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçmək
print([df2['A'][i] for i in range(len(df2['A'])) if df2['A'][i] > 1])
