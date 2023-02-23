string = input("Введіть рядок-> ")
reverse_string = string[::-1]
if string == reverse_string:
    print("Це паліндром")
else:
    print("Це не паліндром")
