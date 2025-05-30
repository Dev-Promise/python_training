
def calulator(num1, num2):
    # 足し算 
    sum_result = num1 + num2 
    print(f"{num1} + {num2} = {sum_result}")

    # 引き算 
    diff_result = num1 - num2 
    print(f"{num1} - {num2} = {diff_result}")

    # 掛け算 
    mul_result = num1 * num2 
    print(f"{num1} * {num2} = {mul_result}")

    # 割り算 
    if num2 == 0:
        print("0除算はできません")
    else:
        div_result = num1 / num2 
        print(f"{num1} / {num2} = {div_result}")

i = 0
while i < 5:
    num1 = float(input("1つ目の数字を入力してください： "))
    num2 = float(input("2つ目の数字を入力してください： "))
    calulator(num1, num2)
    i += 1