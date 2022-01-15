# GUI sub file

import ssh
import timetable_frame
import look_timetable
import owner
import configuration_frame
import subjects_frame
import send_tables_frame
import tkinter as tk

# ボタンクリック時の操作


def reference_attend_data():
    """
    「出席状況」button was pushed
    Notes
    powershellを開き、出席データを格納している機器へアクセス

    """
    pass


def take_photo_command():
    """
    「教室撮影」button was pushed
    """

    # raspberrypiのファイルのパスワードファイルの読み込み
    with open("raspberrypi_key.txt", mode="r") as fp:
        l_strip = [s.strip() for s in fp.readlines()]

    # 呼び出すコマンド
    cmd = 'aac take_photo gui'

    ssh.connect_SSH(
        IP_ADDRESS=l_strip[0], USER_NAME=l_strip[1], PASSWORD=l_strip[2], CMD=cmd
    )


def set_timetable():
    """
    「タイムテーブルの新規作成」button was pushed

    Notes
        新しく時間割を作成する
        「タイムテーブルの名前」と「タイムテーブル」を新たなウィンドウで入力させ、
        指定したフォーマットでテキストファイルに出力する。
    """

    new_window = tk.Toplevel()
    new_window.geometry("750x600")

    timetable_frame.TimetableFrame(new_window)


def set_calender():
    """
    「タイムテーブルの指定」button was pushed
    """
    pass


def looktimetable():
    """
    「タイムテーブル」を見る
    """
    new_window = tk.Toplevel()
    new_window.geometry("750x680")

    look_timetable.LookTimetable(new_window)


def configuration(mysettings: owner.Owner):
    """
    「設定」button was pushed
    Notes
    """
    new_window = tk.Toplevel()
    new_window.geometry("500x550")

    configuration_frame.ConfigurationFrame(new_window, mysettings)

def set_subjects():
    """
    「時間割」の科目名を設定
    """
    new_window = tk.Toplevel()
    new_window.geometry("750x600")

    subjects_frame.SubjectsFrame(new_window)

def send_tables():
    """
    作成したタイムテーブルや時間割のラズパイへの送信
    """
    new_window = tk.Toplevel()
    new_window.geometry("750x600")

    send_tables_frame.SendTablesFrame(new_window)
