import tkinter as tk
from tkinter import ttk, messagebox
import re


class ActivityRegistration:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("羽动天下及民和安五一节活动报名系统")
        self.window.geometry("500x600")

        # 创建表单组件
        self.create_widgets()

    def create_widgets(self):
        # 标题
        title_label = ttk.Label(self.window, text="活动报名表", font=('微软雅黑', 16))
        title_label.pack(pady=20)

        # 表单字段
        fields = [
            ("姓名", "entry", True),
            ("手机号", "entry", True),
            ("邮箱", "entry", False),
            ("性别", "combobox", True),
            ("参与人数", "spinbox", True),
            ("活动时段", "combobox", True),
            ("备注", "text", False)
        ]

        self.entries = {}
        for field in fields:
            frame = ttk.Frame(self.window)
            frame.pack(fill=tk.X, padx=20, pady=5)

            label = ttk.Label(frame, text=f"{field[0]}:", width=10)
            label.pack(side=tk.LEFT)

            if field[1] == "entry":
                entry = ttk.Entry(frame)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries[field[0]] = entry
            elif field[1] == "combobox":
                values = ["男", "女"] if field[0] == "性别" else ["上午场", "下午场", "全天"]
                combobox = ttk.Combobox(frame, values=values, state="readonly")
                combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries[field[0]] = combobox
            elif field[1] == "spinbox":
                spinbox = ttk.Spinbox(frame, from_=1, to=10)
                spinbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries[field[0]] = spinbox
            elif field[1] == "text":
                text = tk.Text(frame, height=4)
                text.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries[field[0]] = text

        # 提交按钮
        submit_btn = ttk.Button(self.window, text="提交报名", command=self.submit_form)
        submit_btn.pack(pady=20)

    def validate_phone(self, phone):
        return re.match(r'^1[3-9]\d{9}$', phone)

    def validate_email(self, email):
        return re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)

    def submit_form(self):
        # 数据收集
        data = {
            "姓名": self.entries["姓名"].get().strip(),
            "手机号": self.entries["手机号"].get().strip(),
            "邮箱": self.entries["邮箱"].get().strip(),
            "性别": self.entries["性别"].get(),
            "参与人数": self.entries["参与人数"].get(),
            "活动时段": self.entries["活动时段"].get(),
            "备注": self.entries["备注"].get("1.0", tk.END).strip()
        }

        # 验证必填字段
        if not data["姓名"]:
            messagebox.showerror("错误", "姓名不能为空！")
            return
        if not self.validate_phone(data["手机号"]):
            messagebox.showerror("错误", "请输入有效的手机号！")
            return
        if data["邮箱"] and not self.validate_email(data["邮箱"]):
            messagebox.showerror("错误", "邮箱格式不正确！")
            return

        # 显示填写内容
        result = "报名信息已提交：\n"
        result += "\n".join([f"{k}: {v}" for k, v in data.items() if v])
        messagebox.showinfo("提交成功", result)


if __name__ == "__main__":
    app = ActivityRegistration()
    app.window.mainloop()