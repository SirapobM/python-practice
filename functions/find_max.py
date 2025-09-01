# ฟังก์ชันหาค่ามากที่สุดใน list
def find_max(numbers):
    max_v = numbers[0]
    for i in numbers:
        if i > max_v:
            max_v = i
    return max_v

nums1 = [10, 25, 7, 3]
nums2 = [-5, -10, -3]

print(find_max(nums1))  # 25
print(find_max(nums2))  # -3
