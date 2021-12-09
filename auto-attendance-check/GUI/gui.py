#Use under Python3.8
import tkinter as tk
from tkinter import Canvas, ttk
from pathlib import Path
from tkinter.constants import FLAT, GROOVE, LEFT, RAISED, RIDGE, SOLID, TOP

#Add tkdesigner to path

#Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

class Maniplation():
    def RefAttendData():
        """
        「出席状況」button was pushed

        Notes
        powershellを開き、出席データを格納している機器へアクセス
        
        """
        None

    def TakePhotoCom():
        """
        「教室撮影」button was pushed
        
        Notes
        powershellを開き、ラズパイにSSH接続
        →ラズパイへ撮影を命令　撮影した教室の画像を画像処理部の画像フォルダに格納する
        →撮影した画像はPC側にも送信　GUI操作者による確認を可能に
        →ラズパイへ画像解析を命令
        →ラズパイとのSSH接続を終了
        """
        None

    def SetTimetable():
        """
        「時間割」button was pushed
        """
        None

    def Configuration():
        """
        「設定」button was pushed
        Notes
        """
        None


#class Application(tk.Frame):
# set up main window
window = tk.Tk()
window.title('MANIPLATION')
window.geometry("754x1080")
#window.geometry("2000x2000")

# set up main frame
frame = ttk.Frame(window)
frame.pack(fill = tk.BOTH, padx=20, pady=10)


# make widgets
#make Canvas
background = tk.PhotoImage(file="AI.png")
canvas = tk.Canvas(
    window,
    width=754,
    height=1080
)
canvas.create_image(377, 540, image=background)

RAD_button = tk.Button(
    frame,
    text="出席状況",
    borderwidth=10,
    padx=60,
    pady=18,
    width=12,
    height=2,
    anchor="w",
    relief=RAISED,
    cursor="hand2",
    command=Maniplation.RefAttendData
)

TPC_button = tk.Button(
    frame,
    text="教室撮影",
    borderwidth=10,
    padx=60,
    pady=18,
    width=12,
    height=2,
    anchor="w",
    relief=RAISED,
    cursor="hand2",
    command=Maniplation.TakePhotoCom
)

ST_button = tk.Button(
    frame,
    text="時間割",
    borderwidth=10,
    padx=60,
    pady=18,
    width=12,
    height=2,
    anchor="w",
    relief=RAISED,
    cursor="hand2",
    command=Maniplation.SetTimetable
)

Conf_button = tk.Button(
    frame,
    text="設定",
    borderwidth=10,
    padx=60,
    pady=18,
    width=12,
    height=2,
    anchor="w",
    relief=RAISED,
    cursor="hand2",
    command=Maniplation.Configuration
)

# set widgets
canvas.pack()
RAD_button.pack(padx=10, pady=20, anchor=tk.W)
TPC_button.pack(padx=10, pady=20, anchor=tk.W)
ST_button.pack(padx=10, pady=20, anchor=tk.W)
Conf_button.pack(padx=10, pady=20, anchor=tk.W)

# show main window

if __name__ == "__main__":
    window.mainloop()