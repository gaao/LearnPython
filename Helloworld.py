#-*- coding: utf-8 -*-

print("hello world")

# 运行
# python Helloworld.py


# 解释性、弱类型语言和 js 比较像
# 字符串的格式化输出
from curses.ascii import isdigit
from this import s


name = 'gxg'
age = 18
gender = '男'
# %s给字符串占位，%d给十进位整型数字占位，%f给浮点数占位
s = "名字 %s，年龄 %d，性别 %s"%( name, age, gender )
print(s)


# 3、索引
# 支持正负索引 语法格式 数据对象 [索引]、数据对象 [开始索引：结束索引]、数据对象 [开始索引：结束索引:step=1] 默认从左往后一个一个的
t = 'hello world!'
print(t[3]) # l
print(t[3:5])# lo
print(t[3:])# lo world!# 冒号右侧缺省代表取到最后
print(t[:3])# hel# 冒号左边缺省代表索引 0 开始
print(t[:])# hello world!#完整
print(t[5:3])# ！必须符合从左到右切
print(t[-6:-1])# world
print(t[-6:])# world!
print(t[-3:-5])# 结果为空

#步长为负从左向右切
print(t[::-1])# !dlrow olleh 倒着排
print(t[6:0:-1])# w olle 
print(t[4::-1])# olleh 想取到 h 应该是缺省

print(t[::2])# hlowrd

#in 判断
print('world'in t)
#拼接
print(t + s)

print(t * 10)

# 4、字符串是内置方法
# upper 大写    lower 小写
# startswith 判断是否以某字符开始  endswith 判断是否以某字符结束
# isdigit 判断是否是数字字符串
# split join 拼接
l = "beijing，shanghai，shengzhen，guangzhou"
ret = l.split("，")
print(ret)

ret1 = '；'.join(ret)
print(ret1)
