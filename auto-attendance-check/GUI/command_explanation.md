> Written with [StackEdit](https://stackedit.io/).

> # SSH接続した際に実行するコマンド集

> 更新 : 2022/01/14

> -  take_photo
	> 教室を撮影
	> core/main.pyのtake_photo() 関数内ですること
	 	> analysis.pyを実行
	    > ↓そのファイル内で写真撮影命令
	    > ↓画像解析
	 	> ↓export.py
        > 引数に 'gui' と入っていた場合（aac take_photo gui）、撮影した画像をGUI部へ送信する（送信先の場所については要相談）

> - send_attend_data
    > 現在の出欠状況を示したファイルをGUI部へ送信する（送信先の場所については要相談）
    > 引数で csv か json のどちらのファイルを送信するか選択できるようにする（例. aac send_attend_data csv）

> - change_crontab
    > core/change_crontab 内の関数 update_schedule を実行する

> - ※タイムテーブルとか時間割ファイルを送信する際はGUI部の方で直接 /user/bin/aac/time_table or subjects/ に送信するようプログラムに書くことにする
> - ※学校では crontabに書き込むファイルphoto_tableはcore内に置くと言ったが、やっぱり分かりやすくするため photo_tableも /user/bin/aac/photo_table/ 内に送信するようにする
