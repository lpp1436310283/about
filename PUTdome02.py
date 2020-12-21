import re
#目标字符串
s="""Hello
武汉
"""
#\w只匹配ascii字符
result=re.findall(r"\w+",s,re.A)
print(result)
#忽略大小写
result=re.findall(r"[a-z]+",s,re.I)
print(result)
#可以换行匹配
result=re.findall(r".+",s,re.S)
print(result)
#让^ $表示每一行的开头结尾
result=re.findall(r"^\w+",s,re.M)

print(result)