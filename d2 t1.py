a=0
b=0
c=0
d=0
s=input("输入字符串:")
for i in s:
    if i.isalpha():
        a+=1
    elif i.isspace():
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print(f"字母数目为:{a},空格数目为:{b},数字数目为:{c},其它字符数目为:{d}")