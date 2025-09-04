# def sayHello(user, age = 20):
#     print("สวัสดี", user, age)

# time = "ตอนเช้า"

# sayHello(time, 14)

#args / kwargs
# ข้อมูลแบบลำดับ *args 
# ข้อมูลแบบกำหนดชื่อ *kwargs
# def saveEmploter(**kwargs):
#     print(f"ชื่อ : {kwargs["name"]} อายุ: {kwargs["age"]} ที่อยู่: {kwargs["address"]}")

# saveEmploter(name="ไม้", age=21, address="ไทย")

#return function
# def get():
#     return 2

# data = get()
# print(f"num : {data}")

# para + return
# def checknum(number):
#     if number%2==0:
#         return "เลขคู่"
#     else: 
#         return "เลขคี่"
    
# result = checknum(3)
# print(result)

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1,2,3))