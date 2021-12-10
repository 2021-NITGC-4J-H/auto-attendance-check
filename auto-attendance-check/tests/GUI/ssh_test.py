# test ssh.py

import ssh

if __name__ == "__main__":
    ssh.ConnectSSH(
        IP_ADDRESS='192.168.2.103',
        USER_NAME='pi',
        PASSWORD='Pottunchin8ma',
        CMD='uname -a'
)