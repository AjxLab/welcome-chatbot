# -*- coding: utf-8 -*-


bot_msg = '話しかけてください'

# 入力 <-> 応答
while True:
    # Botメッセージを表示
    print('Bot：%s' % bot_msg)
    # Botへメッセージを送る
    usr_msg = input('You：')

    # 挨拶
    words = ['はじめまして', 'こんにちは', 'おはよう', 'こんにちは', 'こんばんは']
    for w in words:
        if w in usr_msg:
            bot_msg = w
            break

    # 自己紹介
    words = ['私の名前は', '僕の名前は', '俺の名前は']
    for w in words:
        if w in usr_msg:
            name = usr_msg.replace(w, '').replace('です', '').replace('。', '')
            bot_msg = 'こんにちは。%sさん' % name
            break

    # 終了
    words = ['終了', 'さようなら', '帰って']
    for w in words:
        if w in usr_msg:
            print('Bot：さようなら，また遊んでくださいね。')
            exit(0)

