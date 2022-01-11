import tkinter as tk
import maniplation as man

""" frame_timetable 作成部 """


def change_main_frame(frame: tk.Frame):
    frame.tkraise()


class SubFrame(tk.Frame):
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

        set_timetable_button = tk.Button(
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
            command=man.set_timetable,
        )

        set_timetable_button.pack(padx=5, pady=10, side=tk.TOP)

        set_calender_button = tk.Button(
            self,
            text="時間割の指定",
            borderwidth=10,
            padx=40,
            pady=15,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=man.set_calender,
        )
        set_calender_button.pack(padx=5, pady=10, side=tk.TOP)

        look_timetable_button = tk.Button(
            self,
            text="時間割を見る",
            borderwidth=10,
            padx=40,
            pady=15,
            width=12,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            command=man.look_timetable,
        )
        look_timetable_button.pack(padx=5, pady=10, side=tk.TOP)

        self.grid(row=0, column=0, sticky="nsew")
