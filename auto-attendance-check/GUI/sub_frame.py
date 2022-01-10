import tkinter as tk
import maniplation as man

""" frame_timetable 作成部 """


def changeMainFrame(frame: tk.Frame):
    frame.tkraise()


class subFrame(tk.Frame):
    def __init__(self, window: tk.Tk, frame: tk.Frame):
        super().__init__(window, width=754, height=680)

        # サブウィンドウのbuttonの作成
        button_change = tk.Button(
            self,
            text="メインウィンドウに移動",
            command=self.destroy
            # command=changeMainFrame(frame)
        )
        button_change.pack()

        SetTimetable_button = tk.Button(
            self,
            text="時間割の新規登録",
            # image=new_table_img,
            borderwidth=10,
            padx=40,
            pady=15,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=man.SetTimetable,
        )

        SetTimetable_button.pack(padx=5, pady=10, side=tk.TOP)

        SetCalender_button = tk.Button(
            self,
            text="時間割の指定",
            borderwidth=10,
            padx=40,
            pady=15,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=man.SetCalender,
        )
        SetCalender_button.pack(padx=5, pady=10, side=tk.TOP)

        LookTimetable_button = tk.Button(
            self,
            text="時間割を見る",
            borderwidth=10,
            padx=40,
            pady=15,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=man.LookTimetable,
        )
        LookTimetable_button.pack(padx=5, pady=10, side=tk.TOP)

        self.grid(row=0, column=0, sticky="nsew")
