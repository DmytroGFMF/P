text = input("Введіть текст-> ")
reserved = input("Введіть список зарезервованих слів через кому-> ").split(",")

for i in reserved:
    text = text.replace(i, i.upper())

print("Змінений текст:")
print(text)
