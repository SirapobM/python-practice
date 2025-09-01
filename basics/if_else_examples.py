# Example: Check even or odd
number = int(input("ใส่ตัวเลข: "))
if number % 2 == 0:
    print("ตัวเลขนี้เป็นเลขคู่")
else:
    print("ตัวเลขนี้เป็นเลขคี่")

# Example: Login system
user = input("Username: ")
password = input("Password: ")

if user == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
