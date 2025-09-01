# ฟังก์ชันตรวจสอบว่าเป็นเลขคู่หรือไม่
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(2))  # True
print(is_even(5))  # False
