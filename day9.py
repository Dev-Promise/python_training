import random
import string

def check_strength(pw):
    length = len(pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)

    types = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and types == 4:
        return "強い (Strong)"
    elif length >= 8 and types >= 3:
        return "普通 (Medium)"
    else:
        return "弱い (Weak)"

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        pw = ''.join(random.choice(chars) for _ in range(length))
        if (
            any(c.isupper() for c in pw) and
            any(c.isdigit() for c in pw) and
            any(c in string.punctuation for c in pw)
        ):
            return pw

# ユーザー入力
length = int(input("パスワードの長さを入力してください: "))
count = 5  # 5個生成

print("\n✅ 生成されたパスワード（強度表示付き）:")
for i in range(count):
    pw = generate_password(length)
    strength = check_strength(pw)
    print(f"{i+1}. {pw} → {strength}")
