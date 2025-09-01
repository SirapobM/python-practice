# Banking service with simple menu
user = input("Username: ")
password = input("Password: ")

if user == "member" and password == "1234":
    print("เข้าสู่ระบบสำเร็จ")
    num = int(input("เลข 1 ถอนเงิน, เลข 2 ฝากเงิน: "))
    if num == 1:
        print("ถอนเงิน")
    elif num == 2:
        print("ฝากเงิน")
    else:
        print("หมายเลขบริการไม่ถูกต้อง")
else:
    print("ไม่พบบัญชี")
