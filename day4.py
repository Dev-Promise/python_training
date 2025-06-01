# 書き込み 
with open("day4.txt", "w", encoding="utf-8") as f:
	f.write("これはPythonで書き込んだテキストです。\n")     
	f.write("2行目の内容です。\n")  
	print("書き込みが完了しました。")  

# 追記
with open("day4.txt", mode='a', encoding="utf-8") as f:
	f.write("これはPythonで追記したテキストです。\n")     
	print("追記が完了しました。")  

# 逆順
with open("day4.txt", mode='a', encoding="utf-8") as f:
	a = "逆順のテストです！"[::-1]
	f.write(a)

# 読み込み 
with open("day4.txt", "r", encoding='utf-8') as f:     
	content = f.readlines()  
	
print("ファイルの内容:") 
print(content)