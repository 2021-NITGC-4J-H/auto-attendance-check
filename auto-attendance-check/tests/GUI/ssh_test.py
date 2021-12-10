# test ssh.py

from core.ssh import ConnectSSH

if __name__ == "__main__":
    ssh.ConnectSSH(
        IP_ADDRESS='ip アドレス',
        USER_NAME='ユーザーネーム',
        PASSWORD='パスワード',
        CMD='uname -a'
)