from enum import Enum, auto
import fire


class SaveImage(Enum):
    GUI = auto()
    LOCAL = auto()


class Commands(object):
    """
    auto-attendance-checkのAPI
    sshでCLI実行する目的

    Note
    ----
    GUIの操作に対応させて必要なコマンドを作っていく
    """

    def attend_data():
        """
        ?
        """
        pass

    def take_photo(save_image: SaveImage = SaveImage.LOCAL):
        """
        写真を撮影
        """
        if save_image == SaveImage.LOCAL:
            pass
        elif save_image == SaveImage.GUI:
            pass

    def set_time_table():
        """
        時間割の設定
        """
        pass

    def configuration():
        """
        ?
        """
        pass


if __name__ == "__main__":
    fire.Fire(Commands)
