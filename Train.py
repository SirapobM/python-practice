# กำหนด str -> int, float ....
# x = 1000
# y = "2000"
# print(x + int(y))
# print(x + float(y))

# วิธีหาเลข คู่ และ คี่
# number = int(input("ใส่ตัวเลข : "))
# print("ตัวเลขของคุณคือ : ", number)

# if number%2 == 0:
#     print("ตัวเลขนี้เป็นเลขคู่")
# else:
#     print("ตัวเลขนี้เป็นเลขคี่")

# a = True
# b = False
# print(a and a)

# โจทย์ปัญหา : การล็อกอินเข้าสู่ระบบ
# User = input("Username : ")
# Password = input("Password : ")
# if User == "admin" and Password == "1234":
#     print("Login successful")
# elif User == "admin" or Password == "1234":
#     print("Login successful")
# else:
#     print("Login failed")

# โปรแกรมตัดเกรดอย่างง่าย
# score = int(input("ใส่คะแนนของคุณ : "))
# grade = None

# if score >= 80 and score <= 100:
#     grade = "A"
# elif score >= 70 and score <= 79:
#     grade = "B"
# elif score >= 0 and score <= 69:
#     grade = "F"
# else: 
#     grade = "N"

# print("Your grade is:", grade)

# โจทย์ บริการธนาคาร
# user = input("Username : ")
# password = input("Password : ")

# print("เข้าสู่ระบบสำเร็จ")
# if user == "member" and password == "1234":
#     print("เลข 1 ถอนเงิน, เลข 2 ฝากเงิน")
#     num = int(input("เลือกทำรายการ : "))
#     if num == 1:
#         print("ถอนเงิน")
#     elif num == 2:
#         print("ฝากเงิน")
#     else:
#         print("หมายเลขบริการไม่ถูกต้อง")
# else:
#     print("ไม่พบบัญชี")

# บริการธนาคาร แบบใช้ case
# user = input("Username : ")
# password = input("Password : ")

# if user == "member" and password == "1234":
#     print("เข้าสู่ระบบสำเร็จ")
#     service = int(input("เลข 1 ถอนเงิน, เลข 2 ฝากเงิน, เลข 3 ยอดเงินคงเหลือ : "))
#     match service:
#         case 1:
#             print("ถอนเงิน")
#         case 2:
#             print("ฝากเงิน")
#         case 3:
#             print("ยอดเงินคงเหลือ")
#         case _:
#             print("หมายเลขบริการไม่ถูกต้อง")
# else:
#     print("ไม่พบบัญชี")

# counter = 0
# while counter < 5:
#     counter += 1
#     print(counter)

# for num in range(0,6,2):
#     print(num)

# for num in range(1,10):
#     if num % 3 == 0:
#         continue
#     print(num)

# แสดงสูตรแม่สูตรคูณ
# num = int(input("ใส่เลขที่ต้องการดูสูตรคูณ : "))
# for i in range(1, 13):
#     print(num, "x", i, "=", num*i)

# แสดงสูตรคูณ
# num = int(input("ใส่เลขที่ต้องการดูสูตรคูณ : "))
# count = int(input("ใส่จำนวนที่ต้องการดูรอบสูตรคูณ : "))
# for i in range(1, count+1):
#     print(num, "x", i, "=", num*i)

# โจทย์หาผลรวม 5 ตัวเลข
# sum = 0
# for i in range(1, 6):
#     num = int(input("ใส่ตัวเลข : "))
#     sum += num
# print("ผลรวมของตัวเลขทั้ง 5 ตัว คือ : ", sum)

# total = 0
# while True:
#     number = int(input("ใส่ตัวเลข (0 เพื่อหยุด) : "))
#     if number == 0:
#         break
#     total += number
# print("ผลรวมของตัวเลขทั้งหมด คือ : ", total)

# for i in range(2):
#     print(i)
#     for j in range(3):
#         print(j)

# start = int(input("ใส่จุดเริ่มต้น : "))
# end = int(input("ใส่จุดสิ้นสุด : "))

# for i in range(start, end+1):
#     for j in range(1, 13):
#         print(i, "x", j, "=", i*j)

# name = "Mai Sirapob"
# print(name[1:5])

# fname = "Mai"
# lname = "Rak"

# fullname = fname + " " + lname
# print(fullname)

# address = """
# 123 Main St, Springfield, USA
# """

# print(address)

# year = 2546
# mes = f"เกิดเมื่อ พ.ศ. {year}"
# year = 2003
# print(mes)
# print(type(mes))

# หาตัวอักษรว่าตัวที่เท่าไร
# text = "Mai Sirapob"
# for i in range(len(text)):
#     if text[i] == 'p':
#         print(i)
#         break

# text = "Sirapob"
# print(text.index('p')) F error
# print(text.find('p')) F no error

# month = input("ป้อนเดือน : ")
# if month.endswith("คม"):
#     print("เดือนนี้มี 31 วัน")
# elif month.endswith("ยน"):
#     print("เดือนนี้มี 30 วัน")

# format วันที่
# date = input("ป้อนวันที่ (ปปปป/ดด/วว) : ")
# year, month, day = date.split("/")
# date = "วัน{2} เดือน{1} ปี{0}".format(year, month, day)
# print(date)

# color = ["red", "blue", "green"]
# color.append("yellow") เพิ่ม 1 ตัว
# color.extend(["black", "white"]) เพิ่มหลายตัว
# color.insert(1, "orange") เพิ่มตำแหน่ง index ตัว element
# color.remove("blue")  # ลบ element
# color.clear() ลบทั้งหมด
# color.sort()  # เรียงจากน้อยไปมาก
# color.reverse()  # เรียงจากมากไปน้อย
# print(color)

# color = ("แดง", "เขียว", "น้ำเงิน")
# red, green, blue = color
# print(red)

# animals = {
#     "dog": "สุนัข",
#     "cat": "แมว",
#     "fish": "ปลา"
# }

# print(animals.keys())  # แสดงคีย์ทั้งหมด
# print(animals.values())  # แสดงค่าทั้งหมด
# print(animals.items())  # แสดงคีย์และค่าทั้งหมด

# colorA = ["แดง", "เขียว", "น้ำเงิน"]
# colorB = ["ชมพู", "ม่วง", "ฟ้า"]

# print(colorA is colorB)

# colorA = ["แดง", "เขียว", "น้ำเงิน"]
# print("แดง" in colorA)

# Function
# number = int(input("ใส่เลขที่ต้องการดูสูตรคูณ : "))

# def showTable():
#     for i in range(1, 13):
#         print(f"{number} x {i} = {number*i}")

# showTable()

