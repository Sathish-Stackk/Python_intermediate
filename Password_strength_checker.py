password = "Python@123"

if len(password) < 8:
    print("Weak Password")
elif password.isalnum():
    print("Add Special Characters")
elif not any(char.isdigit() for char in password):
    print("Add Numbers")
else:
    print("Strong Password")
