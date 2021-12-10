# test ssh.py
import sys
import os
from GUI.ssh import ConnectSSH

sys.path.append("../../..")

if __name__ == "__main__":
    ssh.ConnectSSH(
        IP_ADDRESS='ip アドレス',
        USER_NAME='ユーザーネーム',
        PASSWORD='パスワード',
        CMD='uname -a'
)