# maniplation.py > Configuration() により呼び出されるフレーム

import tkinter as tk
import owner


class configurationFrame(tk.Frame):
    """
    mainframeの「設定」 -> maniplation.Configuration() により作成されるフレーム
    """

    def __init__(self, newWindow: tk.Toplevel, mysettings: owner.owner):
        super().__init__(newWindow, width=500, height=550)

        """
        user = tk.Label(self, text="ユーザーネーム : ")
        school = tk.Label(self, text="学校名 : ")
        classname = tk.Label(self, text="クラス名 : ")
        interval = tk.Label(self, text="授業中の撮影間隔 : ")
        """

        self.username_text = tk.StringVar(self)
        self.username_text.set("ユーザーネーム : " + mysettings.username)
        self.schoolname_text = tk.StringVar(self)
        self.schoolname_text.set("学校名 : " + mysettings.schoolname)
        self.classname_text = tk.StringVar(self)
        self.classname_text.set("クラス名 : " + mysettings.classname)
        self.interval_text = tk.StringVar(self)
        self.interval_text.set("授業中の撮影間隔 : " + str(mysettings.interval))

        self.username_label = tk.Label(self, textvariable=self.username_text)
        self.username_label.pack(padx=170, pady=20, side=tk.TOP)
        self.schoolname_label = tk.Label(self, textvariable=self.schoolname_text)
        self.schoolname_label.pack(padx=170, pady=20, side=tk.TOP)
        self.classname_label = tk.Label(self, textvariable=self.classname_text)
        self.classname_label.pack(padx=170, pady=20, side=tk.TOP)
        self.interval_label = tk.Label(self, textvariable=self.interval_text)
        self.interval_label.pack(padx=170, pady=20, side=tk.TOP)

        self.cancel_button = tk.Button(
            self,
            text="完了",
            borderwidth=10,
            padx=15,
            pady=5,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=newWindow.destroy,
        )
        self.cancel_button.pack(padx=100, pady=20, side=tk.BOTTOM)

        self.edit_button = tk.Button(
            self,
            text="編集",
            borderwidth=10,
            padx=15,
            pady=5,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=lambda: self.EditData(newWindow, mysettings),
        )
        self.edit_button.pack(padx=100, pady=20, side=tk.BOTTOM)

        self.grid(row=0, column=0, sticky="nsew")

    def EditData(self, toplevel: tk.Toplevel, mysettings: owner.owner):
        """
        「個人設定」を変更する関数
        """
        editFrame = tk.Frame(toplevel, width=500, height=750)
        change = []

        self.errortext = tk.StringVar(self)
        self.errorlabel = tk.Label(
            editFrame, textvariable=self.errortext, fg="red", font=("Arial", 20)
        )
        self.errorlabel.place(x=5, y=260)

        change.append(tk.Entry(editFrame, width=30))
        change.append(tk.Entry(editFrame, width=30))
        change.append(tk.Entry(editFrame, width=30))
        change.append(tk.Entry(editFrame, width=30))

        username_label = tk.Label(editFrame, text="ユーザーネーム : ")
        username_label.place(x=80, y=50)
        change[0].place(x=200, y=50)
        schoolname_label = tk.Label(editFrame, text="学校名 : ")
        schoolname_label.place(x=80, y=100)
        change[1].place(x=200, y=100)
        classname_label = tk.Label(editFrame, text="クラス名 : ")
        classname_label.place(x=80, y=150)
        change[2].place(x=200, y=150)
        interval_label = tk.Label(editFrame, text="授業中の撮影間隔 : ")
        interval_label.place(x=80, y=200)
        change[3].place(x=200, y=200)

        cancel_button = tk.Button(
            editFrame,
            text="キャンセル",
            borderwidth=10,
            padx=15,
            pady=5,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=editFrame.destroy,
        )
        cancel_button.place(x=150, y=360)

        complete_button = tk.Button(
            editFrame,
            text="変更",
            borderwidth=10,
            padx=15,
            pady=5,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=lambda: self.Update(editFrame, mysettings, change),
        )
        complete_button.place(x=290, y=360)

        editFrame.grid(row=0, column=0, sticky="nsew")

    def Update(self, editFrame: tk.Frame, mysettings: owner.owner, change: tk.Entry):
        """
        ラベルに入力された値から設定情報を更新する

        return:
            Success -> 0
            Failure -> -1
        """
        new_interval = change[3].get()
        if new_interval == "":
            new_interval = -1
        else:
            try:
                new_interval = int(new_interval)
            except ValueError as e:
                print(e)
                self.errorlabel.config(bg="lightslategray")
                self.errortext.set("撮影間隔には数字を入力してください")
                return -1

        mysettings.Update(
            username=change[0].get(),
            schoolname=change[1].get(),
            classname=change[2].get(),
            interval=new_interval,
        )

        self.username_text.set("ユーザーネーム : " + mysettings.username)
        self.schoolname_text.set("学校名 : " + mysettings.schoolname)
        self.classname_text.set("クラス名 : " + mysettings.classname)
        self.interval_text.set("授業中の撮影間隔 : " + str(mysettings.interval))

        editFrame.destroy()

        return 0
