import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import ttkbootstrap as ttkb
import pandas as pd
from PIL import ImageTk, Image

# 正在尝试排版
#   ·画网格
#   °ppt放置控件

# 正在尝试植入到主程序中
# 学习数据处理pandas


        # fpath = "F:\AspenTest\耦合工艺20230413\Result1.xlsx"
        # result = pd.read_excel(fpath)
        # result.set_index(["Unnamed: 2"], inplace=True)
        # result = result.drop(labels=['Unnamed: 0', 'Unnamed: 1'], axis=1)
        # # result = result.drop(labels=['From'], axis=0)
        # print(result)
        # # print(result.loc[['From', 'Description'], 'Unnamed: 3'])

# ///////////////////////实例化//////////////////////////
root = tk.Tk()
style = ttkb.Style("morph")
root.title("Aspen设置")
root.geometry("800x500")
note = Notebook(root, width=800, height=500)

# 添加标题图片
img = Image.open('标题.png')
photo = ImageTk.PhotoImage(img)
imglabel = Label(root, image=photo)
imglabel.place(x=0, y=0)

fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

note.place(x=0, y=70)

note.add(fr1, text='input')
note.add(fr2, text='result')
note.add(fr3, text='...')

# 构建fr1框架（用canvas）


# 构建网格
label = tk.Label(fr1, text="1")
label.place(x=0, y=0)
label = tk.Label(fr1, text="2")
label.place(x=100, y=0)
label = tk.Label(fr1, text="3")
label.place(x=200, y=0)
label = tk.Label(fr1, text="4")
label.place(x=300, y=0)
label = tk.Label(fr1, text="5")
label.place(x=400, y=0)
label = tk.Label(fr1, text="6")
label.place(x=500, y=0)
label = tk.Label(fr1, text="7")
label.place(x=600, y=0)
label = tk.Label(fr1, text="8")
label.place(x=700, y=0)

label = tk.Label(fr1, text="1")
label.place(x=0, y=100)
label = tk.Label(fr1, text="2")
label.place(x=0, y=200)
label = tk.Label(fr1, text="3")
label.place(x=0, y=300)

# base method
label = tk.Label(fr1, text="Base method:", font=('等线', 15))
label.place(x=280, y=10)
method = tk.StringVar()
choice = tk.ttk.Combobox(fr1, textvariable=method, values=["IDEAL", "PENG-ROB"], font=('等线', 12), width=10)
choice.current(0)
choice.place(x=400, y=9)

labFrame1 = Labelframe(fr1, text='烟气入口条件')  # 此处为避免放不下控件不能设置固定的宽高，但可以通过控制控件大小来控制宽高
labFrame1.place(x=90, y=60)
label = tk.Label(labFrame1, text="   ")
label.grid(row=1, column=0)
# 状态变量（温度）-文本框
label = tk.Label(labFrame1, text="温度：")
label.grid(row=2, column=0)
fume_temperature = tk.IntVar()
fume_temperatureInput = tk.Entry(labFrame1, textvariable=fume_temperature)
fume_temperatureInput.grid(row=2, column=1, sticky='w')
label = tk.Label(labFrame1, text="°C", height=1)
label.grid(row=2, column=2, sticky='w')
# 状态变量（压力）
label = tk.Label(labFrame1, text="压力：")
label.grid(row=3, column=0)
fume_pressure = tk.DoubleVar()
fume_pressureInput = tk.Entry(labFrame1, textvariable=fume_pressure)
fume_pressureInput.grid(row=3, column=1)
label = tk.Label(labFrame1, text="MPa")
label.grid(row=3, column=2, sticky='w')
# 总流率
label = tk.Label(labFrame1, text="总流率:")
label.grid(row=4, column=0)
total_flow_rate = tk.DoubleVar()
TotalFlowRateInput = tk.Entry(labFrame1, textvariable=total_flow_rate)
TotalFlowRateInput.grid(row=4, column=1)
label = tk.Label(labFrame1, text="scmh (Mole)")
label.grid(row=4, column=2, sticky='w')
# 组分设置
label = tk.Label(labFrame1, text="   ")
label.grid(row=5, column=0)
label = tk.Label(labFrame1, text="输入组分")
label.grid(row=6, column=0, sticky='w')
label = tk.Label(labFrame1, text="(Mass-Frac)")
label.grid(row=6, column=1, sticky='w')
label = tk.Label(labFrame1, text="H2O：")
label.grid(row=7, column=0)
fume_H2O = tk.DoubleVar()
H2OInput = tk.Entry(labFrame1, textvariable=fume_H2O)
H2OInput.grid(row=7, column=1)
label = tk.Label(labFrame1, text="N2：")
label.grid(row=8, column=0)
fume_N2 = tk.DoubleVar()
N2Input = tk.Entry(labFrame1, textvariable=fume_N2)
N2Input.grid(row=8, column=1)
label = tk.Label(labFrame1, text="CO2：")
label.grid(row=9, column=0)
fume_CO2 = tk.DoubleVar()
CO2Input = tk.Entry(labFrame1, textvariable=fume_CO2)
CO2Input.grid(row=9, column=1)
label = tk.Label(labFrame1, text="O2：")
label.grid(row=10, column=0)
fume_O2 = tk.DoubleVar()
O2Input = tk.Entry(labFrame1, textvariable=fume_O2)
O2Input.grid(row=10, column=1)


# 冷源入口条件
labFrame2 = Labelframe(fr1, text="冷源入口条件")
labFrame2.place(x=420, y=60)
# 状态变量
label = tk.Label(labFrame2, text="   ")
label.grid(row=1, column=0)
# 状态变量（温度）-文本框
label = tk.Label(labFrame2, text="温度：")
label.grid(row=2, column=0)
coldsource_temperature = tk.IntVar()
temperatureInput = tk.Entry(labFrame2, textvariable=coldsource_temperature)
temperatureInput.grid(row=2, column=1)
label = tk.Label(labFrame2, text="°C")
label.grid(row=2, column=2, sticky='w')
# 状态变量（压力）
label = tk.Label(labFrame2, text="压力：")
label.grid(row=3, column=0)
coldsource_pressure = tk.DoubleVar()
pressureInput = tk.Entry(labFrame2, textvariable=coldsource_pressure)
pressureInput.grid(row=3, column=1)
label = tk.Label(labFrame2, text="MPa")
label.grid(row=3, column=2, sticky='w')
# 总流率
label = tk.Label(labFrame2, text="总流率：")
label.grid(row=4, column=0)
coldsource_total_flow_rate = tk.DoubleVar()
TotalFlowRateInput = tk.Entry(labFrame2, textvariable=coldsource_total_flow_rate)
TotalFlowRateInput.grid(row=4, column=1)
label = tk.Label(labFrame2, text="scmh (Mole)")
label.grid(row=4, column=2, sticky='w')
label = tk.Label(labFrame2, text="   ")
label.grid(row=5, column=0)

# 绘制确定设置按钮
combobox_button = tk.Button(fr1, text="确定")
combobox_button.place(x=540, y=220)

# 绘制运行按钮
run_button = tk.Button(fr1, text="运行Aspen")
run_button.place(x=470, y=260)
# # 绘制结束按钮
close_button = tk.Button(fr1, text="关闭Aspen")
close_button.place(x=573, y=260)

root.mainloop()