# 1から10までの2乗のリストを作る
squares = [x**2 for x in range(1, 11)]
print(squares)

# 1から20までの偶数だけを集める
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# 文字列リストを大文字に変換する
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words)

# 数字とその2乗の辞書を作る（1から5）
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

# 既存の辞書から特定の条件のものだけを抽出する
prices = {"apple": 100, "banana": 80, "cherry": 120}
high_prices = {fruit: price for fruit, price in prices.items() if price >= 100}
print(high_prices)

# ネストしたリスト（2次元）を1次元にflattenする
nested_list = [[1, 2, 3], [4, 5], [6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# 辞書のキー・値を入れ替える辞書を作る
d = {'a': 1, 'b': 2, 'c': 3}
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)
