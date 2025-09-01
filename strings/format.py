# จัดรูปแบบวันที่
date = input("ป้อนวันที่ (ปปปป/ดด/วว) : ")
year, month, day = date.split("/")
date_fmt = "วัน{2} เดือน{1} ปี{0}".format(year, month, day)
print(date_fmt)