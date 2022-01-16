from enum import Enum, auto
import fire
from analysis import face_detection, take_photo
from export import ClassMatesRegister
from change_crontab import update_schedule

class SaveImage(Enum):
    """
    撮影した画像の保存先を指定するenum
    Commands.take_photo()の引数

    Attributes
    ----------
    GUI
        GUIclientからこの引数付きでコマンドが呼ばれた場合、撮影した画像をGUIclientに送信する
    LOCAL
        撮影した画像をローカルフォルダに保存する
    """
    GUI = auto()
    LOCAL = auto()


class ExportDataType(Enum):
    """
    出欠状況をエクスポートするときに選択可能なファイルのタイプ

    Attributes
    ----------
    CSV
        csvの出欠状況ファイルを選択
    JSON
        jsonの出欠状況ファイルを選択
    """
    CSV = auto()
    JSON = auto()


class Commands(object):
    """
    auto-attendance-checkのAPI
    sshでCLI実行する目的

    Note
    ----
    GUIの操作に対応させて必要なコマンドを作っていく
    """
    def take_photo(save_image: SaveImage = SaveImage.LOCAL, save_path: str = "~/Picture/"):
        """
        写真を撮影

        Parameters
        ----------
        save_image : SaveImage
            画像の保存先指定する
        """
        img = take_photo()
        if save_image == SaveImage.LOCAL:
            pass
        elif save_image == SaveImage.GUI:
            pass

    def analysis():
        """
        撮影した画像の解析を行う
        """
        # res = face_detection(img)
        pass

    def sent_attend_date(data_type: ExportDataType):
        """
        この関数が実行された時点での最新出欠状況をGUIclientにSSHで送信する
        引数でjson,csvを選択する
        """
        regi = ClassMatesRegister(number_of_students=0)
        if data_type == ExportDataType.CSV:
            regi.exprot_csv()
        elif data_type == ExportDataType.JSON:
            regi.export_json()

    def update_crontab():
        """
        google calendar からこの関数が実行されたときの日にちの時間割を取得し、crontabを変更する
        """
        update_schedule()


def main():
    fire.Fire(Commands)
