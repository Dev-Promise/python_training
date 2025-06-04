import datetime
import calendar


# 今日の日付を取得
today = datetime.date.today()
year = today.year
month = today.month
day = today.day

# カレンダーの月表示（テキスト形式）
cal = calendar.TextCalendar()

# 表示する月のカレンダーを取得
month_str = cal.formatmonth(year, month)
highlighted = []

# 今日の日付にアスタリスクをつけて強調表示
for line in month_str.split("\n"):
    if str(day) in line.split():
        # 数字を揃えるため、1桁・2桁で分岐
        line = line.replace(f"{day:2d}", f"*{day:2d}")
    highlighted.append(line)

# 出力
print("\n".join(highlighted))


year = datetime.date.today().year
print(calendar.calendar(year))
