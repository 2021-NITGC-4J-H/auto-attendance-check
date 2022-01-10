# 作成した時間割を見る

import tkinter as tk
import glob
import os
import timetable_frame


class look_timetable(tk.Frame):
    """
    mainframeの「時間割」 -> subframeの「時間割を見る」
    ボタンが押された時に作成するフレーム
    """

    def __init__(self, newWindow: tk.Toplevel):
        super().__init__(newWindow, width=754, height=1080)

        self.toplevel = newWindow

        # 時間割フォルダ内のファイル情報を取得する
        path_list, name_list, num = self.filesearch("./class_table")

        self.titlelabel = tk.Label(self, text="クリックした時間割を表示します")
        self.titlelabel.place(x=300, y=30)

        self.name_text = []
        self.name_label = []
        self.selectbox = []

        for i in range(0, num):
            self.name_text.append(tk.StringVar(self))
            self.name_text[i].set(name_list[i])
            self.name_label.append(
                tk.Label(self, textvariable=self.name_text[i], font=("Times", 14))
            )

            if i == 0:
                self.selectbox.append(
                    tk.Button(
                        self,
                        text="表示",
                        command=lambda: self.LookTable(self.name_text[0].get()),
                    )
                )
            elif i == 1:
                self.selectbox.append(
                    tk.Button(
                        self,
                        text="表示",
                        command=lambda: self.LookTable(self.name_text[1].get()),
                    )
                )
            elif i == 2:
                self.selectbox.append(
                    tk.Button(
                        self,
                        text="表示",
                        command=lambda: self.LookTable(self.name_text[2].get()),
                    )
                )
            elif i == 3:
                self.selectbox.append(
                    tk.Button(
                        self,
                        text="表示",
                        command=lambda: self.LookTable(self.name_text[3].get()),
                    )
                )

            self.name_label[i].place(x=150, y=(120 + (100 * i)))
            self.selectbox[i].place(x=300, y=(120 + (100 * i)))

            i = i + 1

        self.finish_button = tk.Button(
            self,
            text="終了",
            borderwidth=10,
            padx=15,
            pady=5,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=newWindow.destroy,
        )
        self.finish_button.place(x=600, y=900)

        self.grid(row=0, column=0, sticky="nsew")

    def filesearch(self, dir: str):
        """
        引数に指定したディレクトリ配下のファイルを探す関数

        return:
            path_list: パス名のリスト
            name_list: (拡張子なしの)ファイル名のリスト
            num: ファイル数
        """
        # 指定dir内のすべてのファイルを取得
        path_list = glob.glob(dir + "/*")

        # パスリストからファイル名を抽出
        num = 0
        name_list = []
        for i in path_list:
            file = os.path.basename(i)
            name, ext = os.path.splitext(file)
            name_list.append(name)
            print(str(i) + i)
            num += num + 1

        num = num - 1
        return path_list, name_list, num

    def LookTable(self, tablename: str):
        """
        時間割を表示(編集)する

        return :
            Success -> 0
            Failure -> -1
        """

        editFrame = timetable_frame.timetableFrame(self.toplevel)

        # 指定された時間割の内容を取得
        try:
            with open(
                "./class_table/" + tablename + ".txt", "rt", encoding="UTF-8"
            ) as fp:
                data = fp.readlines()
        except FileNotFoundError as e:
            print(e)
            return -1

        textname = data[0].split("\n")

        editFrame.name_text.insert(0, textname[0])

        for i in range(0, int(data[1])):
            time = data[2 + (i * 2)].split()
            editFrame.start_hour[i].set(time[0])
            editFrame.start_min[i].set(time[1])

            time = data[2 + (i * 2 + 1)].split()
            editFrame.end_hour[i].set(time[0])
            editFrame.end_min[i].set(time[1])

        pass
