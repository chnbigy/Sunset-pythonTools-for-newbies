import os
# -*- coding:utf-8 -*-
from tkinter import Tk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror

if __name__ != "__main__":
    pass
else:
    showinfo(title="Sunset Python Tools Available Queries1.0.0",
             message="Welcome Sunset pytools Available Queries\n version For 1.0.0\n Now I will help you Test!\n If you You ready\n Press "
                     "this button")

print("现在开始，你只需要和步骤走就可以当代码没结束时请按下Enter继续")
input("Welcome Use This Tools,Now I'm going to help you see if you have these necessary things ")
print("one,python Test")
a=os.system("Python -V")
print(a)

print("阶段2")
input("pip Test")
b=os.system("pip -V")
print(b)
print("three,Location of pip ")
c=os.system("where pip")
print(c)

print("End,If the above code does not report an error,You can use the tool with confidence")
print("结束，如果上述代码没有问题那么你就可以放心使用工具了！")
input("按下任意键exit")
exit(0)