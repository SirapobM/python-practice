# ฟังก์ชันหาค่าน้อยที่สุดใน list
def find_min(numbers):
    min_v = numbers[0]
    for i in numbers:
        if i < min_v:
            min_v = i
    return min_v

nums = [2, 3, 5, 10]
print(find_min(nums))  # 2
