# def sayHello(user, age = 20):
#     print("สวัสดี", user, age)

# time = "ตอนเช้า"

# sayHello(time, 14)

#args / kwargs
# ข้อมูลแบบลำดับ *args 
# ข้อมูลแบบกำหนดชื่อ *kwargs
def saveEmploter(**kwargs):
    print(f"ชื่อ : {kwargs["name"]} อายุ: {kwargs["age"]} ที่อยู่: {kwargs["address"]}")

saveEmploter(name="ไม้", age=21, address="ไทย")