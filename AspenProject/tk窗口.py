import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import ttkbootstrap as ttkb
import pandas as pd

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

fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

note.place(x=0, y=0)

note.add(fr1, text='input')
note.add(fr2, text='result')
note.add(fr3, text='...')

label = tk.Label(fr1, text="Base method:")
label.place(x=10, y=10)
method = tk.StringVar()
choice = tk.ttk.Combobox(fr1, textvariable=method, values=["IDEAL", "PENG-ROB"])
choice.current(0)
choice.place(x=100, y=10)

labFrame1 = Labelframe(fr1, text='烟气入口条件', width=100)
labFrame1.place(x=45, y=60)
label1 = tk.Label(labFrame1, text="状态变量", width=10)
label1.grid(row=0, column=0, padx=20, pady=5)
# 状态变量（温度）-文本框
label = tk.Label(labFrame1, text="温度：")
label.grid(row=1, column=0)
fume_temperature = tk.IntVar()
fume_temperatureInput = tk.Entry(labFrame1, textvariable=fume_temperature)
fume_temperatureInput.grid(row=1, column=1)
label = tk.Label(labFrame1, text="C")
label.grid(row=1, column=2)
# 状态变量（压力）
label = tk.Label(labFrame1, text="压力：")
label.grid(row=2, column=0)
fume_pressure = tk.DoubleVar()
fume_pressureInput = tk.Entry(labFrame1, textvariable=fume_pressure)
fume_pressureInput.grid(row=2, column=1)
label = tk.Label(labFrame1, text="MPa")
label.grid(row=2, column=2)
# 总流率
label = tk.Label(labFrame1, text="总流率:")
label.grid(row=3, column=0)
total_flow_rate = tk.DoubleVar()
TotalFlowRateInput = tk.Entry(labFrame1, textvariable=total_flow_rate)
TotalFlowRateInput.grid(row=3, column=1)
label = tk.Label(labFrame1, text="scmh (Mole)")
label.grid(row=3, column=2)
#
# # 组分设置
# label = tk.Label(labFrame1, text="输入组分：(Mass-Frac)")
# label.grid(row=5, column=0)
# label = tk.Label(labFrame1, text="H2O：")
# label.grid(row=6, column=0)
# fume_H2O = tk.DoubleVar()
# H2OInput = tk.Entry(labFrame1, textvariable=fume_H2O)
# H2OInput.grid(row=6, column=1)
#
# label = tk.Label(labFrame1, text="N2：")
# label.grid(row=7, column=0)
# fume_N2 = tk.DoubleVar()
# N2Input = tk.Entry(labFrame1, textvariable=fume_N2)
# N2Input.grid(row=7, column=1)
#
# label = tk.Label(labFrame1, text="CO2：")
# label.grid(row=8, column=0)
# fume_CO2 = tk.DoubleVar()
# CO2Input = tk.Entry(labFrame1, textvariable=fume_CO2)
# CO2Input.grid(row=8, column=1)
#
# label = tk.Label(labFrame1, text="O2：")
# label.grid(row=9, column=0)
# fume_O2 = tk.DoubleVar()
# O2Input = tk.Entry(labFrame1, textvariable=fume_O2)
# O2Input.grid(row=9, column=1)
#
#
# # 冷源入口条件
# label = tk.Label(fr1, text="冷源入口条件")
# label.grid(row=13, column=0)
# # 状态变量
# label = tk.Label(fr1, text="状态变量")
# label.grid(row=14, column=0)
#
# # 状态变量（温度）-文本框
# label = tk.Label(fr1, text="温度：")
# label.grid(row=15, column=0)
# coldsource_temperature = tk.IntVar()
# temperatureInput = tk.Entry(fr1, textvariable=coldsource_temperature)
# temperatureInput.grid(row=15, column=1)
# label = tk.Label(fr1, text="C")
# label.grid(row=15, column=2)
# # 状态变量（压力）
# label = tk.Label(fr1, text="压力：")
# label.grid(row=16, column=0)
# coldsource_pressure = tk.DoubleVar()
# pressureInput = tk.Entry(fr1, textvariable=coldsource_pressure)
# pressureInput.grid(row=16, column=1)
# label = tk.Label(fr1, text="MPa")
# label.grid(row=16, column=2)
# # 总流率
# label = tk.Label(fr1, text="总流率")
# label.grid(row=17, column=0)
# coldsource_total_flow_rate = tk.DoubleVar()
# TotalFlowRateInput = tk.Entry(fr1, textvariable=coldsource_total_flow_rate)
# TotalFlowRateInput.grid(row=17, column=1)
# # TotalFlowRate = TotalFlowRateInput.get()
# label = tk.Label(fr1, text="scmh (Mole)")
# label.grid(row=17, column=2)
#
# # 绘制确定设置按钮
# combobox_button = tk.Button(fr1, text="确定")
# combobox_button.grid(row=20, column=1)
#
# # 绘制运行按钮
# run_button = tk.Button(fr1, text="运行Aspen")
# run_button.grid(row=21, column=0)
# # 绘制结束按钮
# close_button = tk.Button(fr1, text="关闭Aspen")
# close_button.grid(row=21, column=2)

root.mainloop()