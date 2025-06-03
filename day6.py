import json
import os

TASK_FILE = 'tasks.json'

# タスク読み込み
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'r') as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)

def show_tasks():
    print("\n=== 未完了タスク ===")
    for i, task in enumerate(tasks):
        if not task['done']:
            print(f"{i + 1}. {task['title']}")
    print("\n=== 完了済みタスク ===")
    for i, task in enumerate(tasks):
        if task['done']:
            print(f"{i + 1}. {task['title']}")

while True:
    show_tasks()
    cmd = input("\nコマンドを入力してください (add / done / del / quit): ")

    if cmd == 'add':
        title = input("タスク名を入力: ")
        tasks.append({'title': title, 'done': False})
        save_tasks()
    elif cmd == 'done':
        num = int(input("完了にするタスク番号: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]['done'] = True
            save_tasks()
        else:
            print("無効な番号です。")
    elif cmd == 'del':
        num = int(input("削除するタスク番号: ")) - 1
        if 0 <= num < len(tasks):
            del tasks[num]
            save_tasks()
        else:
            print("無効な番号です。")
    elif cmd == 'quit':
        print("終了します。")
        break
    else:
        print("不明なコマンドです。")
