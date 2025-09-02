# เขียนโปรแกรม รับค่าเลข 2 จำนวนจากผู้ใช้ (เช่น start และ end) แล้วให้โปรแกรม หาผลรวมของเลขคู่ ระหว่าง start ถึง end
num_s = int(input("กรอกค่าเริ่มต้น : "))
num_e = int(input("กรอกค่าสิ้นสุด : "))

def cal(number_s, number_e):
    sum = 0
    for i in range(number_s, number_e+1):
        if i % 2 == 0:
            sum += i
    return sum

# result = cal(num_s, num_e)
# print(f"ผลรวมของเลขคู่ระหว่าง {num_s} ถึง {num_e} คือ {result}")

# เขียนโปรแกรมรับค่าเริ่มต้น (start) และสิ้นสุด (end) จากผู้ใช้ แล้วหาผลรวมของเลขคี่ทั้งหมดในช่วง
num_start = int(input("กรอกค่าเริ่มต้น : "))
num_end = int(input("กรอกค่าสิ้นสุด : "))

def cal(num_s, num_e):
    sum = 0
    for i in range(num_s, num_e+1):
        if i % 2 == 1:
            sum += i
    return sum

result = cal(num_start, num_end)
print(f"ผลรวมเลขคี่ : {result}")

