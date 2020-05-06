import oseti


# ネガポジ分析
# nega(-1.0) <-> posi(1.0)
analyzer = oseti.Analyzer()

score = analyzer.analyze('今日はとてもいい天気です。')
print(score[-1])
