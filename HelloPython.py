# output command
# print("Hello Python World")
# use variable 使用变量
# Python 本身作为高级语言，可以不用添加变量标识与‘；’
# message = "Hello Python World"
# print(message)
# variable name  变量名
# 变量名明明只能包含数字，字母，下划线
# 变量名命名尽量按照驼峰命名法，或是按照统一规范，不要使用简称
# #######################运算符#################################
# 运算符 |  功能 | 用法
# + | 一元正号 | + expr  }一元运算符
# - | 一元负号 | - expr  }一元运算符
# * | 乘法 | expr * expr
# / | 除法 | expr / expr
# % | 取余 | expr % expr
# + | 加号 | expr + expr
# - | 减号 | expr - expr
# 逻辑运算符与关系运算符
# ! | 逻辑非 | !expr }一元运算符
# < | 小于 | expr < expr
# > | 大于 | expr > expr
# <= | 小于等于 | expr <= expr
# >= | 大于等于 | expr >= expr
# == | 相等 | expr == expr
# != | 不相等 | expr != expr
# && | 逻辑与 | expr && expr
# || | 逻辑或 | expr || expr
# 赋值运算符
# = 赋值运算符左侧必须是一个可修改的左值 ex: int i = 0;
# 同时给多个值赋值
x,y,z = 0,0,0
print(f"x:{x} y:{y} z:{z}")
x=y=z=1
print(f"x:{x} y:{y} z:{z}")
# 递增运算符和递减运算符
# ++ | --
# 访问运算符
# . p.size();
# 条件运算符
# ?:  0>1?0:1;
# ####################String 字符串###################################
# 字符串通常使用""/ '' 包围，其实是char值集合
# example:
stringExample = "This is a string example."
print(stringExample)

# properties
# Upper():大写 lower():小写 title():首字母大写
print(stringExample.title())
print(stringExample.lower())
print(stringExample.upper())
# format() 字符串中使用变量
# py3.0以前 format()方法
first_name = "zhang"
last_name = "san"
# c#中$标识符
name = f"{first_name}-{last_name}"
print(name)
# 换行符与制表符
print(f"\tname")
print(f"\nname")
# 删除空白
delete = ' delete '
print(f"This is a test about{delete}!")
# print(delete.lstrip()) 将会出现错误 lstrip()方法具有返回值不对原值修改，需要重新赋予变量
# 但是上述语法再其他语言中可以实现
delete2 = delete.lstrip()
print(f"This is a test about{delete2}!")
print(f"This is a test about delete:{delete}!")

delete3 = delete.rstrip()
print(f"This is a test about{delete3}!")
print(f"len about string: delete:{len(delete)} delete2:{len(delete2)} delete3:{len(delete3)}")
# ################################数###########################
# 整数 int(integer) 适用 +，-，*，/，%等运算符
a = 2+3
b = 2-3
# 浮点数 double/float 带小数点的数，同上
# 任意两个整数相除，得到一个浮点数，一个整数与一个浮点数运算得到浮点数
print(2/1)
print(2*2)
# 当数特别大时，可以使用下划线分割
print(1400_000_001)

# python 之禅
# 漂亮的代码要比杂乱的代码要好
# 显性的要比隐性的好
# 简单要比复杂好
# 现实总是复杂的
# 扁平要比嵌套好
# 稀疏要比密集好
# 简单易读，复杂项目下要编写注释
# 不要因为特殊情况打破本身的规则逻辑
# 实用性胜过炫技
# 错误不应该被静默传递
# 除非明确静默
# 面对模棱两可的地方，不要胡乱猜测
# 通常情况下解决方案只有一个，复杂解决情况最好只有一种，通过明显的路线实现
# 虽然这种方案并不是显而易见的，因为你不是那个荷兰人[这里指的是Python之父Guido]
# 现在开始做比不做好
# 不做比盲目去做好
# 如果一个实现方案难于理解，它就不是一个好的方案
# 如果一个实现方案易于理解，它很有可能是一个好的方案
# 命名空间非常有用，我们应当多加利用
import this

