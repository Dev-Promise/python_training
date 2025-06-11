import requests
from bs4 import BeautifulSoup

# Yahooニュース トップページ
url = "https://news.yahoo.co.jp/"
response = requests.get(url)

# ステータス確認
if response.status_code != 200:
    print("ページ取得に失敗しました")
    exit()

# HTMLを解析
soup = BeautifulSoup(response.text, "html.parser")

# aタグをすべて取得
all_links = soup.find_all("a")

# ニュース候補を保存するリスト
results = []

print("📰 Yahooニュース トップ記事（推定）:")
count = 0
for link in all_links:
    text = link.get_text(strip=True)
    href = link.get("href")
    # 条件に合うリンクだけ抽出
    if (
        text
        and len(text) >= 15  # タイトルっぽい文字数
        and href
        and "news.yahoo.co.jp" in href
    ):
        print(f"- {text}({href})")
        results.append(f"{text} ({href})")
        count += 1
    if count >= 5:
        break

# ✅ ファイルに保存
with open("yahoo_news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("\n📝 ファイル 'yahoo_news.txt' に保存しました！")
