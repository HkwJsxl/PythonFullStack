"""

Python在执行时可能会产生一个字节码文件，当我们执行一个脚本时，脚本引入的模块会产生pyc文件

解释型语言和编译型语言

计算机是不能够识别高级语言的，所以当我们运行一个高级语言程序时，就需要一个“翻译机”来从事把高级语言转变成计算机能够读懂的机器语言的过程。
这个过程分为两类，第一种是编译，第二种是解释

编译型语言在程序执行之前，先会通过编译器对程序执行一个编译的过程，把程序变成机器语言。运行时就不用翻译，而是直接运行就可以了，最典型的是C语言
解释型语言就是没有这个编译的过程，而是在程序运行的时候，通过解释器对程序逐行做出解释，然后直接运行，例如ruby
还有第三种，是Java这种，先编译后解释。

我们的Python也是属于那种先编译后解释的语言，
当Python程序运行时，编译结果则是保存在位于内存中的PyCodeObject中，
当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中。

当Python程序第二次运行时，首先程序会在硬盘上寻找对应的pyc文件，如果找到，则直接载入，否则就重复上面的过程

Python执行的过程：

所以可以认定，Python它面向对象更彻底了，比JAVA中的一切皆对象更彻底，JAVA中有class，也就是类的概念，object是class的一个实例。
但是Python中函数和类也是对象

"""


"""
过程说明
1、Python程序首次运行时，编译的结果保存在内存中的PycodeObject中。
Python程序运行结束时，Python解释器将PycodeObject写回硬盘的pyc文件。
2、Python程序第二次运行时，首先程序会在硬盘中找到pyc文件，如果找到，直接装载，否则重复上述过程。
因此，pyc文件实际上是PyCodeObject的持久保存方式。
也就是说，保存pyc文件是为了避免在下次再次使用该剧本时重复编译，节省时间。因此，只执行一次脚本，就没有必要保存其编译结果pyc文件浪费空间。
"""
