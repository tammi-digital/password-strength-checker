password = input("Enter a password: ")

if len(password) < 8:
    print("Weak password: must be at least 8 characters")
elif password.isalpha():
    print("Medium password: add numbers or symbols")
elif password.isnumeric():
    print("Weak password: use letters and symbols")
else:
    print("Strong password!")
