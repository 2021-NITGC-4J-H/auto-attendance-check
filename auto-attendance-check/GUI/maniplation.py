#GUI sub file

import ssh

#ボタンクリック時の操作

def RefAttendData():
    """
    「出席状況」button was pushed
    Notes
    powershellを開き、出席データを格納している機器へアクセス
    
    """
    pass

def TakePhotoCom():
    """
    「教室撮影」button was pushed
    
    Notes
        powershellを開き、ラズパイにSSH接続
        →ラズパイへ撮影を命令 撮影した教室の画像を画像処理部の画像フォルダに格納する
        →撮影した画像はPC側にも送信 GUI操作者による確認を可能に
        →ラズパイへ画像解析を命令
        →ラズパイとのSSH接続を終了
        
    Variable
    --------
    CMD : str list
        ラズパイへの命令を集めたリスト
        この関数 TakePhotoCom() 内では、
        'rpistill -o /home/pi/rpicamera/rpicamera.sh'
        '画像解析部の呼び出し'
    (/home/pi/rpicamera/rpicamera.sh : 画像撮影命令が記述されているファイル)
    """
    
    """
    今後変更するかもしれない部分
    ラズパイのip,username,passwordをまとめたクラスを作成し、Parameterで渡す
    """

    cmd = []

    ssh.ConnectSSH(
        IP_ADDRESS='192.168.2.103',
        USER_NAME='pi',
        PASSWORD='Pottunchin8ma',
        CMD=cmd
    )



def SetTimetable():
    """
    「時間割」button was pushed
    """
    pass

def Configuration():
    """
    「設定」button was pushed
    Notes
    """
    pass

