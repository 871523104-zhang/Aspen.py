from CodeLibrary import Simulation
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import ttkbootstrap as ttkb
from PIL import ImageTk, Image

# 正在尝试排版
#   ·画网格
#   ·输入控件放置完成
#   °选项卡设置
#   °窗口文件移植到可打开Aspen文件中
#   ·输出方法找到了！！！可以不用导出到excel，而是直接在变量管理器里就能找到！！真的是，原来这么简单。。。

#   底边图片加不上！！！！！！！！！！！！！！！！！！！！！！！9.20

# 正在尝试植入到主程序中
# 学习数据处理pandas


# ///////////////////////实例化//////////////////////////
sim = Simulation(AspenFileName="耦合工艺20230413.apw", WorkingDirectoryPath=r"F:\AspenTest\耦合工艺20230413",
                 VISIBILITY=True)


def result_sim():
    Method = method.get()
    sim.GLB_Set_Method(Method)

    Fume_Temperature = fume_temperature.get()
    sim.FUME_Set_Temperature(Fume_Temperature)
    Fume_Pressure = fume_pressure.get()
    sim.FUME_Set_Pressure(Fume_Pressure)
    Total_Flow_Rate = total_flow_rate.get()
    sim.FUME_Set_Total_Flow_Rate(Total_Flow_Rate)
    Fume_H2O = fume_H2O.get()
    sim.FUME_Set_H2O(Fume_H2O)
    Fume_N2 = fume_N2.get()
    sim.FUME_Set_N2(Fume_N2)
    Fume_CO2 = fume_CO2.get()
    sim.FUME_Set_CO2(Fume_CO2)
    Fume_O2 = fume_O2.get()
    sim.FUME_Set_O2(Fume_O2)

    ColdSource_Temperature = coldsource_temperature.get()
    sim.COLDSOURCE_Set_Temperature(ColdSource_Temperature)
    ColdSource_Pressure = coldsource_pressure.get()
    sim.COLDSOURCE_Set_Pressure(ColdSource_Pressure)
    ColdSource_Total_Flow_Rate = coldsource_total_flow_rate.get()
    sim.COLDSOURCE_Set_Total_Flow_Rate(ColdSource_Total_Flow_Rate)


root = tk.Tk()
style = ttkb.Style("morph")
root.title("Aspen设置")
root.geometry("800x500")
note = Notebook(root, width=800, height=500)

# 添加标题图片
img1 = Image.open(r"F:\AspenPlus-Python-Interface-main\AspenPlus-Python-Interface-main\AspenProject\标题.png")
photo = ImageTk.PhotoImage(img1)
imglabel = Label(root, image=photo)
imglabel.place(x=0, y=0)
# 添加底边图片
# img2 = Image.open(r"F:\AspenPlus-Python-Interface-main\AspenPlus-Python-Interface-main\AspenProject\底边.png")
# global photo2
# photo2 = ImageTk.PhotoImage(img2)
# imglabel2 = Label(root, image=photo2)
# imglabel2.place(x=0, y=400)

fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

note.place(x=0, y=70)

note.add(fr1, text='input')
note.add(fr2, text='result')
note.add(fr3, text='...')


# 构建网格
label = tk.Label(fr2, text="1")
label.place(x=0, y=0)
label = tk.Label(fr2, text="2")
label.place(x=100, y=0)
label = tk.Label(fr2, text="3")
label.place(x=200, y=0)
label = tk.Label(fr2, text="4")
label.place(x=300, y=0)
label = tk.Label(fr2, text="5")
label.place(x=400, y=0)
label = tk.Label(fr2, text="6")
label.place(x=500, y=0)
label = tk.Label(fr2, text="7")
label.place(x=600, y=0)
label = tk.Label(fr2, text="8")
label.place(x=700, y=0)

label = tk.Label(fr2, text="1")
label.place(x=0, y=100)
label = tk.Label(fr2, text="2")
label.place(x=0, y=200)
label = tk.Label(fr2, text="3")
label.place(x=0, y=300)


# base method
label = tk.Label(fr1, text="Base method:", font=('等线', 15))
label.place(x=280, y=10)
method = tk.StringVar()
choice = tk.ttk.Combobox(fr1, textvariable=method, values=["IDEAL", "PENG-ROB"], font=('等线', 12), width=10)
choice.current(0)
choice.place(x=400, y=9)


# 烟气入口条件
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
label = tk.Label(labFrame2, text="kg/hr")
label.grid(row=4, column=2, sticky='w')
label = tk.Label(labFrame2, text="   ")
label.grid(row=5, column=0)


# 绘制确定设置按钮
combobox_button = tk.Button(fr1, text="确定", command=result_sim)
combobox_button.place(x=540, y=220)
# 绘制运行按钮
run_button = tk.Button(fr1, text="运行Aspen", command=sim.EngineRun)
run_button.place(x=470, y=260)
# 绘制结束按钮
close_button = tk.Button(fr1, text="关闭Aspen", command=sim.CloseAspen)
close_button.place(x=573, y=260)


# 绘制输出窗口
label = tk.Label(fr2, text="Temperature：", font="bold")
label.grid(row=0, column=0)
label = tk.Label(fr2, text=sim.GET_RESULT_TEMPERATURE())
label.grid(row=0, column=1)

root.mainloop()
