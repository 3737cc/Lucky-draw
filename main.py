import random
import tkinter as tk

# 定义奖项
PRIZES = {
    "一等奖": (1, 1000),
    "二等奖": (1001, 5000),
    "三等奖": (5001, 20000),
    "再抽一次": (20001, 50000),
    "谢谢参与": (50001, 100000),
}

# 定义概率
PROBABILITY = {
    "一等奖": 0.01,
    "二等奖": 0.04,
    "三等奖": 0.15,
    "再抽一次": 0.3,
    "谢谢参与": 0.5,
}


# 抽奖函数
def lottery():
    # 生成随机数
    random_number = random.randint(1, 100000)

    # 显示随机数
    random_number_label.config(text=f"您的随机数是：{random_number}")

    # 遍历奖项
    for prize, (start, end) in PRIZES.items():
        if start <= random_number <= end:
            # 中奖
            result_label.config(text=f"恭喜您！您抽到的是：{prize}")
            break


# 创建主窗口
root = tk.Tk()
root.title("抽奖程序")
root.geometry("300x200+800+300")

# 创建按钮
start_button = tk.Button(root, text="开始抽奖", command=lottery)
start_button.pack()

# 创建随机数标签
random_number_label = tk.Label(root, text="随机数：")
random_number_label.pack()

# 创建结果标签
result_label = tk.Label(root, text="")
result_label.pack()

# 启动主循环
root.mainloop()
