"""
データのエクスポートを行うモジュール
"""

from enum import Enum
import csv
import json

class AttendanceState(Enum):
    """
    出席の正体を表す列挙体
    
    Attributs
    ---------
    ABSENCE : str
        欠席
    LATENESS : str
        遅刻
    AUTHORIZEED_ABSENCE : str
        公欠
    ATTEND : str
        出席
    ERROR : str
        エラー
    """

    ABSENCE = "absence"
    LATENESS = "lateness"
    AUTHORIZEED_ABSENCE = "authorized absence"
    ATTEND = "attend"
    ERROR = "error"


class ClassRegister():
    """
    クラスの出席状況を管理するクラス

    Attributs
    ---------
    file_path : str
        ファイルの書き出しを行うパス
    data : list
        各学生の学生自身の情報、学生の出席状態を持つリスト

    Example
    -------
    file_path = "./attendance_datas/"
    data = [
        {
            "student number": 20,
            "name": "山田一郎",
            "attandance state": AttendanceState.ATTEND.value
        },
        {
            "student number": 21,
            "name": "山田二郎",
            "attandance state": AttendanceState.ABSENCE.value
        }
    ]
    """

    def __init__(self, number_of_students: int) -> None:
        """
        初期化を行う

        Parameters
        ----------
        number_of_students : int
            クラス当たりの学生数

        Todo
        ----
        データをどう持つべきか
        """
        self.file_path = ""
        self.data = [ { "student number": students_number, "name": "", "attendance state": AttendanceState.ERROR.value } for students_number in range(1, number_of_students + 1)]
        pass

    def exprot_csv(self) -> None:
        """
        csv形式でデータをエクスポートする

        Todo
        ----
        文字列での出力にも対応させる

        Notes
        -----
        書き出すファイルのエンコードはutf-8
        """
        with open(f"{self.file_path}.csv", mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, ["student number", "name", "attendance state"])
            writer.writeheader()
            for parson in self.data:
                writer.writerows(parson)

    def export_json(self) -> None:
        """
        json形式でデータをエクスポートする

        Todo
        ----
        文字列での出力にも対応させる

        Notes
        -----
        書き出すファイルのエンコードはutf-8
        """
        with open(f"{self.file_path}.json", mode="w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
