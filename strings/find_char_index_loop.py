# -------------------------------------------------#
# หาตำแหน่งตัวอักษรด้วยการวนลูป
text = "Mai Sirapob"
for i in range(len(text)):
    if text[i] == 'p':
        print(i)
        break

# -------------------------------------------------#
# เปรียบเทียบ index() กับ find()
text = "Sirapob"
# print(text.index('p')) # ถ้าไม่เจอ -> error
print(text.find('p'))    # ถ้าไม่เจอ -> คืน -1 (ไม่ error)


