import tkinter as tk
from tkinter import ttk
import subprocess
import webbrowser
import tkinter.messagebox
def install_pyinstaller():
    ad_window.destroy()

ad_window = tk.Tk()
ad_window.geometry("600x400")
ad_window.title("Python Tools v2.9.9正式版-用户手册")
label = ttk.Label(ad_window, text="产品作者：Sunset_，\n版本：2.9.9正式版 \n""用途：快速安装一些常用模块，帮助自己节约手资源\n有BUG请反馈给我\n按下下方按钮=你将履行本软件开源免费义务\n 此软件所有的镜像来源于清华大学镜像站https://pypi.tuna.tsinghua.edu.cn/simple/\n如果涉嫌侵权，我必下架此软件", font=("Helvetica", 12))
label.place(relx=0.5, rely=0.4, anchor="center")

exit_button = ttk.Button(ad_window, text="好的我知道了", command=install_pyinstaller)
exit_button.place(relx=0.1, rely=0.93, anchor="center")


exit_button = ttk.Button(ad_window, text="Exit/退出", command=install_pyinstaller)
exit_button.place(relx=0.8, rely=0.9)

tkinter.messagebox.showinfo("Update information/更新信息",
                            "You are currently experiencing version 2.9.9/你正在体验的是2.9.9版本\n1.本次更源新优化了体验新增多个按钮-主要\n 2.Fix List\n -修复代码中一些不和谐元素 \n -码中新加入未完成开发的新功能源码不过现在状态：# \n -修改退出按钮位置从此告别找不到\n -版本提升2.0.0→2.9.9 \n 当前软件解决了2.0.0的图片问题（直接删除了源码-从根源解决了问题）\n Tips本次更新不影响主要功能 \n By Sunset Make \n Sunset PythonTools v2.9.9")

ad_window.mainloop()

def install_pyinstaller():
    # 清空Text组件中的文本
    result_text.delete(1.0, tk.END)

    # 显示进度条
    progress_bar.start()

    # 执行安装命令
    cmd = ["pip", "install", "pyinstaller", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple/"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # 隐藏进度条
    progress_bar.stop()

    # 显示安装结果
    result_text.insert(tk.END, result.stdout)


def install_pyqt():
    # 清空Text组件中的文本
    result_text.delete(1.0, tk.END)

    # 显示进度条
    progress_bar.start()

    # 执行安装命令
    cmd = ["pip", "install", "PyQt5", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple/"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # 隐藏进度条
    progress_bar.stop()

    # 显示安装结果
    result_text.insert(tk.END, result.stdout)


#未上线功能-------------------------------------------------------------------------------------------------------------------------------------

#def pyinstaller():
#    result_text.delete(1.0, tk.END)

 #   progress_bar.start()

  #  cmd = ["pyinstaller", "-V"]

   # result = subprocess.run(cmd, capture_output=True, text=True)

    #progress_bar.stop()

    #result_text.insert(tk.END, result.stdout)

def quit():
    window.destroy()


window = tk.Tk()
window.geometry("700x520")
window.title("Sunset Py Tools v2.9.9正式版")

# 设置Label
label = ttk.Label(window, text="Sunset Python Tools -V2.9.9\n 镜像来自国内清华大学镜像站\n https://pypi.tuna.tsinghua.edu.cn/simple/")
label.pack(pady=20)

# 设置按钮
pyinstaller_button = ttk.Button(window, text="Pip PyInstaller", command=install_pyinstaller)
pyinstaller_button.pack()

pyqt_button = ttk.Button(window, text="Pip PyQt5", command=install_pyqt)
pyqt_button.pack()



def open_website():
    webbrowser.open("https://www.bilibili.com/video/BV1yL411K7CP/")

website_button = ttk.Button(window, text="Tools彩蛋For2.0", command=open_website)
website_button.pack()

def open_website():
    webbrowser.open("https://mirrors.tuna.tsinghua.edu.cn/")

website_button = ttk.Button(window, text="清华镜像站-官网", command=open_website)
website_button.pack()

def btnClick():
    tkinter.messagebox.showinfo("Sunset Py Tools版本信息","当前版本为2.9.9正式版\n如果希望获得更新的版本，请添加我\n 软件by Sunset,如果侵权了我马上配合的删除元素")
btn = tkinter.Button(window, text="关于软件-版本©问题", command=btnClick)
btn.pack()

def btnClick():
    tkinter.messagebox.showinfo("彩蛋","2.x.x版本彩蛋：下方结果栏可以输入~🌹")
btn = tkinter.Button(window, text="彩蛋For2.x.x", command=btnClick)
btn.pack()

label = ttk.Label(window, text="需要官网点按钮，上方提供的是下载源")
label.pack(pady=20)

# 设置结果显示框
result_text = tk.Text(window, width=80, height=14)
result_text.pack(pady=20)

# 设置进度条
progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="indeterminate")



exit_button = ttk.Button(window, text="关闭/Quit", command=quit)
exit_button.place(relx=0.85, rely=0.6)

window.mainloop()





