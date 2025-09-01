# Working with lists
colors = ["red", "blue", "green"]
colors.append("yellow")       # เพิ่ม 1 ตัว
colors.extend(["black", "white"])  # เพิ่มหลายตัว
colors.insert(1, "orange")    # เพิ่มตำแหน่ง index
colors.remove("blue")         # ลบ element
colors.sort()                 # เรียงจากน้อยไปมาก
colors.reverse()              # เรียงจากมากไปน้อย

print(colors)
