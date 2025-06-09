import time

'''
input("Enterキーでスタート！")
start = time.time()

input("Enterキーでストップ！")
end = time.time()

elapsed = end - start
print(f"経過時間は {elapsed:.2f} 秒でした。")

'''

minute = int(input("分を入力してください: "))
second = int(input("秒数を入力してください"))

total_seconds = minute * 60 + second


for i in range(total_seconds, 0, -1):
    minutes, seconds = divmod(i,60)
    print(f"{minutes}分{seconds}秒残り")
    time.sleep(1)
 
print("時間になりました！")

