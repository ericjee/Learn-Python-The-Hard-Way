# -*- coding: utf-8 -*-
name = 'Eric Shen'
age = 25 # not a lie
height = 175 # cm
weight = 65 # KG
eyes = 'Black' # Chinese Man, u know that
teeth = 'White' # Do i have other choices?
hair = 'Black' # I'm a Chinese, I love my country

print "Let's talk about %s." % name
print "He's %s cm tall." % height
print "He's %s KG heavy." % weight
print "Actually that's really slim"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

#格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

# %s    字符串 (采用str()的显示)

# %r    字符串 (采用repr()的显示)

# %c    单个字符

# %b    二进制整数

# %d    十进制整数

# %i    十进制整数

# %o    八进制整数

# %x    十六进制整数

# %e    指数 (基底写为e)

# %E    指数 (基底写为E)

# %f    浮点数

# %F    浮点数，与上相同

# %g    指数(e)或浮点数 (根据显示长度)

# %G    指数(E)或浮点数 (根据显示长度)

# %%    字符"%"

# 可以用如下的方式，对格式进行进一步的控制：

# %[(name)][flags][width].[precision]typecode

# (name)为命名

# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。

# width表示显示宽度

# precision表示小数点后精度

#比如：

# print("%+10x" % 10)
# print("%04d" % 5)
# print("%6.3f" % 2.3)
# 上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：

# print("%.*f" % (4, 1.2))
# Python实际上用4来替换*。所以实际的模板为"%.4f"。

