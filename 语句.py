#-*- coding: utf-8 -*-

name = 'gxg'
age = 18
gender = '男'
# # %s给字符串占位，%d给十进位整型数字占位，%f给浮点数占位
s = "名字 %s，年龄 %d，性别 %s"%( name, age, gender )
print(s)
if name == 'gxg' and age == 18:
  print('信息正确')
else:
  print('false')