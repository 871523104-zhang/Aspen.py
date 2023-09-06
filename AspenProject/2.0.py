import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from CodeLibrary import Simulation
import ttkbootstrap as ttkb

# ////////////////////函数////////////////////////
class myWindow:
    # 定义构造函数，绘制窗体
    def __init__(self, master=None):
        self.coldsource_temperature = None
        self.fume_O2 = None
        self.fume_CO2 = None
        self.fume_N2 = None
        self.fume_H2O = None
        self.total_flow_rate = None
        self.fume_pressure = None
        self.fume_temperature = None
        self.method = None
        self.fr1 = master
        self.fr1.title("Aspen设置")
        self.fr1.geometry("800x500")
        note = Notebook(root, style="danger")
        note.pack(fill="both", expand=True)
        note.grid(row=0)
        fr1 = Frame(root, relief='ridge', borderwidth=1)
        fr2 = Frame(root, relief='ridge', borderwidth=1)
        fr3 = Frame(root, relief='ridge', borderwidth=1)
        note.add(fr1, text='input')
        note.add(fr2, text='result')
        note.add(fr3, text='...')
        self.createWidgets()

    # 定义绘制控件函数
    def createWidgets(self):
        # 绘制method组合选择框
        label = tk.Label(self.fr1, text="Base method:")
        label.grid(row=1, column=1)
        self.method = tk.StringVar()
        choice = tk.ttk.Combobox(self.fr1, textvariable=self.method, values=["IDEAL", "PENG-ROB"])
        choice.current(0)
        choice.grid(row=1, column=2)

        labFrame1 = Labelframe(self.fr1, text='烟气入口条件')
        labFrame1.grid(row=2, column=0)
        label = tk.Label(labFrame1, text="状态变量")
        label.grid(row=1, column=0)
        # 状态变量（温度）-文本框
        label = tk.Label(labFrame1, text="温度：")
        label.grid(row=2, column=0)
        self.fume_temperature = tk.IntVar()
        fume_temperatureInput = tk.Entry(labFrame1, textvariable=self.fume_temperature)
        fume_temperatureInput.grid(row=2, column=1)
        label = tk.Label(labFrame1, text="C")
        label.grid(row=2, column=2)
        # 状态变量（压力）
        label = tk.Label(labFrame1, text="压力：")
        label.grid(row=3, column=0)
        self.fume_pressure = tk.DoubleVar()
        fume_pressureInput = tk.Entry(labFrame1, textvariable=self.fume_pressure)
        fume_pressureInput.grid(row=3, column=1)
        label = tk.Label(labFrame1, text="MPa")
        label.grid(row=3, column=2)
        # 总流率
        label = tk.Label(labFrame1, text="总流率:")
        label.grid(row=4, column=0)
        self.total_flow_rate = tk.DoubleVar()
        TotalFlowRateInput = tk.Entry(labFrame1, textvariable=self.total_flow_rate)
        TotalFlowRateInput.grid(row=4, column=1)
        label = tk.Label(labFrame1, text="scmh (Mole)")
        label.grid(row=4, column=2)

        # 组分设置
        label = tk.Label(labFrame1, text="输入组分：(Mass-Frac)")
        label.grid(row=5, column=0)
        label = tk.Label(labFrame1, text="H2O：")
        label.grid(row=6, column=0)
        self.fume_H2O = tk.DoubleVar()
        H2OInput = tk.Entry(labFrame1, textvariable=self.fume_H2O)
        H2OInput.grid(row=6, column=1)

        label = tk.Label(labFrame1, text="N2：")
        label.grid(row=7, column=0)
        self.fume_N2 = tk.DoubleVar()
        N2Input = tk.Entry(labFrame1, textvariable=self.fume_N2)
        N2Input.grid(row=7, column=1)

        label = tk.Label(labFrame1, text="CO2：")
        label.grid(row=8, column=0)
        self.fume_CO2 = tk.DoubleVar()
        CO2Input = tk.Entry(labFrame1, textvariable=self.fume_CO2)
        CO2Input.grid(row=8, column=1)

        label = tk.Label(labFrame1, text="O2：")
        label.grid(row=9, column=0)
        self.fume_O2 = tk.DoubleVar()
        O2Input = tk.Entry(labFrame1, textvariable=self.fume_O2)
        O2Input.grid(row=9, column=1)


        # 冷源入口条件
        label = tk.Label(self.fr1, text="冷源入口条件")
        label.grid(row=13, column=0)
        # 状态变量
        label = tk.Label(self.fr1, text="状态变量")
        label.grid(row=14, column=0)

        # 状态变量（温度）-文本框
        label = tk.Label(self.fr1, text="温度：")
        label.grid(row=15, column=0)
        self.coldsource_temperature = tk.IntVar()
        temperatureInput = tk.Entry(self.fr1, textvariable=self.coldsource_temperature)
        temperatureInput.grid(row=15, column=1)
        label = tk.Label(self.fr1, text="C")
        label.grid(row=15, column=2)
        # 状态变量（压力）
        label = tk.Label(self.fr1, text="压力：")
        label.grid(row=16, column=0)
        self.coldsource_pressure = tk.DoubleVar()
        pressureInput = tk.Entry(self.fr1, textvariable=self.coldsource_pressure)
        pressureInput.grid(row=16, column=1)
        label = tk.Label(self.fr1, text="MPa")
        label.grid(row=16, column=2)
        # 总流率
        label = tk.Label(self.fr1, text="总流率")
        label.grid(row=17, column=0)
        self.coldsource_total_flow_rate = tk.DoubleVar()
        TotalFlowRateInput = tk.Entry(self.fr1, textvariable=self.coldsource_total_flow_rate)
        TotalFlowRateInput.grid(row=17, column=1)
        # TotalFlowRate = TotalFlowRateInput.get()
        label = tk.Label(self.fr1, text="scmh (Mole)")
        label.grid(row=17, column=2)

        # 绘制确定设置按钮
        combobox_button = tk.Button(self.fr1, text="确定", command=self.result_sim)
        combobox_button.grid(row=20, column=1)

        # 绘制运行按钮
        run_button = tk.Button(self.fr1, text="运行Aspen", command=sim.EngineRun)
        run_button.grid(row=21, column=0)
        # 绘制结束按钮
        close_button = tk.Button(self.fr1, text="关闭Aspen", command=sim.CloseAspen)
        close_button.grid(row=21, column=2)

        # 设置闪蒸计算类型
        #label = tk.Label(self.master, text="闪蒸计算类型")
        #label.grid(row=1, column=0)

    # 响应函数：获得当前选择选项，##使用var.get()来获得目前选项内容
    def result_sim(self):
        Method = self.method.get()
        sim.GLB_Set_Method(Method)

        Fume_Temperature = self.fume_temperature.get()
        sim.FUME_Set_Temperature(Fume_Temperature)
        Fume_Pressure = self.fume_pressure.get()
        sim.FUME_Set_Pressure(Fume_Pressure)
        Total_Flow_Rate = self.total_flow_rate.get()
        sim.FUME_Set_Total_Flow_Rate(Total_Flow_Rate)
        Fume_H2O = self.fume_H2O.get()
        sim.FUME_Set_H2O(Fume_H2O)
        Fume_N2 = self.fume_N2.get()
        sim.FUME_Set_N2(Fume_N2)
        Fume_CO2 = self.fume_CO2.get()
        sim.FUME_Set_CO2(Fume_CO2)
        Fume_O2 = self.fume_O2.get()
        sim.FUME_Set_O2(Fume_O2)

        ColdSource_Temperature = self.coldsource_temperature.get()
        sim.COLDSOURCE_Set_Temperature(ColdSource_Temperature)
        ColdSource_Pressure = self.coldsource_pressure.get()
        sim.COLDSOURCE_Set_Pressure(ColdSource_Pressure)
        ColdSource_Total_Flow_Rate = self.coldsource_total_flow_rate.get()
        sim.COLDSOURCE_Set_Total_Flow_Rate(ColdSource_Total_Flow_Rate)

# ///////////////////////实例化//////////////////////////
sim = Simulation(AspenFileName="耦合工艺20230413.apw",
                         WorkingDirectoryPath=r"F:\AspenTest\耦合工艺20230413",
                         VISIBILITY=True)
root = tk.Tk()
style = ttkb.Style("morph")
setting_window = myWindow(root)
root.mainloop()
