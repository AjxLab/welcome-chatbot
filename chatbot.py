#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markovify
from janome.tokenizer import Tokenizer
import wakalinus
import re
import requests


# ネガポジ分析
# nega(-1.0) <-> posi(1.0)
analyzer = wakalinus.Analyzer()
# マルコフ連鎖の学習済みモデル
model = markovify.Text.from_json(open('model/model.json').read())
# 形態素解析器
tagger = Tokenizer()

bot_msg = '話しかけてください'

# 入力 <-> 応答
while True:
    # Botメッセージを表示
    print('Bot：%s' % bot_msg)
    # Botへメッセージを送る
    print('')
    usr_msg = input('You：')

    # 応答済みか
    called = False

    # 挨拶
    if tagger.tokenize(usr_msg)[0].part_of_speech.split(',')[0] == '感動詞':
        bot_msg = tagger.tokenize(usr_msg)[0].surface + '。'
        called = True
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

    # ダジャレ
    words = ['ダジャレ', '地口', 'ジョーク']
    for w in words:
        if w in usr_msg:
            url = 'https://script.google.com/macros/s/AKfycbx2h8jWePcUxszENqm4EqO7gk1bMDqGQKOUSPfQkDKtdwfoxAM/exec?randNum=1'
            res = requests.get(url)
            bot_msg = res.json()['jokes'][0]['joke']
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

    # ネガティブな発言
    if analyzer.analyze(usr_msg)[-1] < 0.0:
        bot_msg = 'あまり気を落とさないでください。。'
        called = True
    if called:  continue

    # 文章生成
    try:
        start = tagger.tokenize(usr_msg)[0].surface
        bot_msg = model.make_sentence_with_start(beginning=start).replace(' ', '')
        called = True
    except:
        pass
    if called:  continue

    # マッチしない場合
    bot_msg = 'すみません，よくわかりません。'

