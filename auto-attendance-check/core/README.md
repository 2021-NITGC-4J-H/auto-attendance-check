# core

## 使用方法

```sh
NAME
    main.py - auto-attendance-checkのAPI sshでCLI実行する目的

SYNOPSIS
    main.py COMMAND

DESCRIPTION
    Note
    ----
    GUIの操作に対応させて必要なコマンドを作っていく

COMMANDS
    COMMAND is one of the following:

     analysis
       撮影した画像の解析を行う

     sent_attend_date
       この関数が実行された時点での最新出欠状況をGUIclientにSSHで送信する 引数でjson,csvを選択する

     take_photo
       写真を撮影

     update_crontab
       google calendar からこの関数が実行されたときの日にちの時間割を取得し、crontabを変更する
```
