# -------------------------------------------------#
# ตัวอย่างการทำงานกับ list
color = ["red", "blue", "green"]
color.append("yellow")                 # เพิ่ม 1 ตัว
color.extend(["black", "white"])       # เพิ่มหลายตัว
color.insert(1, "orange")              # เพิ่มที่ index 1
color.remove("blue")                   # ลบ element
# color.clear()                        # ลบทั้งหมด
color.sort()                           # เรียงจากน้อยไปมาก (ตามลำดับตัวอักษร)
color.reverse()                        # กลับลำดับ (มากไปน้อย)
print(color)

# -------------------------------------------------#
# ตัวอย่าง tuple และการ unpack
color = ("แดง", "เขียว", "น้ำเงิน")
red, green, blue = color
print(red)

# -------------------------------------------------#
# ตัวอย่าง dictionary
animals = {
    "dog": "สุนัข",
    "cat": "แมว",
    "fish": "ปลา"
}

print(animals.keys())    # คีย์ทั้งหมด
print(animals.values())  # ค่า (values) ทั้งหมด
print(animals.items())   # คู่ (key, value) ทั้งหมด

# -------------------------------------------------#
# identity vs membership
colorA = ["แดง", "เขียว", "น้ำเงิน"]
colorB = ["ชมพู", "ม่วง", "ฟ้า"]

print(colorA is colorB)        # เปรียบ "เป็นลิสต์เดียวกันไหม" (อ้างอิงหน่วยความจำ)

colorA = ["แดง", "เขียว", "น้ำเงิน"]
print("แดง" in colorA)         # ตรวจสมาชิกอยู่ในลิสต์ไหม
