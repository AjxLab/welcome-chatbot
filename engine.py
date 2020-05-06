import markovify

model = markovify.Text.from_json(open('model/model.json').read())
print(model.make_sentence_with_start(beginning='私').replace(' ', ''))
