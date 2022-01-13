# google calendar から今日の時間割を取得し、crontabを変更

"""
毎日午前0時になったらこのファイルを実行する
"""

import google_calendar
import datetime
import glob
import os
from typing import Tuple


def file_search(dir: str) -> Tuple[list, list, int]:
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
    num = len(path_list)
    name_list = []
    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        name_list.append(name)
        print(str(i) + i)

    return path_list, name_list, num


def main() -> bool:
    """
    google calendar から今日の時間割を取得し、crontabを変更する
    """
    events = google_calendar.read()

    if not events:
        print("No upcoming events fountd.")
        return False

    now = datetime.datetime.utcnow().isoformat() + "Z"
    time = now.split("T")
    path_list, name_list, num = file_search("./photo_table")

    i = 0
    for event in events:
        i = 0
        start = event["start"].get("dateTime", event["start"].get("date"))
        if start in time[0]:
            while (i < num) and (event["summary"] != name_list[i]):
                i += 1
            if i < num:
                break

    print("num==", num)
    print("i==", i)
    if event["summary"] != name_list[i]:
        print("Couldn't find match event")
        return False

    os.system('crontab /home/pi/core/photo_table/' + event['summary'] + '.txt')

    return True


if __name__ == "__main__":
    main()
