# โจทย์ปัญหา : การล็อกอินเข้าสู่ระบบ
User = input("Username : ")
Password = input("Password : ")
if User == "admin" and Password == "1234":
    print("Login successful")
elif User == "admin" or Password == "1234":
    # หมายเหตุ: เงื่อนไขนี้จะผ่านถ้าอย่างน้อยตรงเงื่อนไขหนึ่ง -> ไม่ปลอดภัย
    print("Login successful")
else:
    print("Login failed")
