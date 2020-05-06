# -*- coding: utf-8 -*-
import oseti
import engine

# ネガポジ分析
# nega(-1.0) <-> posi(1.0)
analyzer = oseti.Analyzer()

bot_msg = '話しかけてください'


# 入力 <-> 応答
while True:
    # Botメッセージを表示
    print('Bot：%s' % bot_msg)
    # Botへメッセージを送る
    usr_msg = input('You：')

    # 応答済みか
    called = False

    # 挨拶
    words = ['はじめまして', 'こんにちは', 'おはよう', 'こんにちは', 'こんばんは']
    for w in words:
        if w in usr_msg:
            bot_msg = w
            called = True
            break
    if called:  continue

    # 自己紹介
    words = ['私の名前は', '僕の名前は', '俺の名前は']
    for w in words:
        if w in usr_msg:
            name = usr_msg.replace(w, '').replace('です', '').replace('。', '')
            bot_msg = 'こんにちは。%sさん' % name
            called = True
            break
    if called:  continue

    # 終了
    words = ['終了', 'さようなら', '帰って']
    for w in words:
        if w in usr_msg:
            print('Bot：さようなら，また遊んでくださいね。')
            exit(0)
    if called:  continue

    if analyzer.analyze(usr_msg)[-1] < 0.0:
        bot_msg = 'あまり気を落とさないでください。。'
        called = True
    if called:  continue

    print(engine.make_reply(usr_msg))


    # マッチしない場合
    bot_msg = 'すみません，よくわかりません。'

