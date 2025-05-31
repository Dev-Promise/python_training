
text = input("文字列を入力してください: ")  

# 文字列を逆順にする 
normalized_text = text.replace(" ", "").lower()
reversed_text = normalized_text[::-1] 

if normalized_text == reversed_text:     
	print("回文です！") 
else:     
	print("回文ではありません。")
	

"""
text1 = input("1つ目の文字列を入力してください: ") 
text2 = input("2つ目の文字列を入力してください: ")  
if sorted(text1.replace(" ", "").lower()) == sorted(text2.replace(" ", "").lower()):     
	print("アナグラムです！") 
else:     
	print("アナグラムではありません。")
"""