import re

with open('raw_data/test.txt', 'r') as file:
    for line in file.readlines():
        sentence_count = line.count('.')
        words = line.split(' ')
        word_count = len(words)
        letters = line.split()
        #regex to remove any punctuation for letter counts
        line = re.sub(r"[-', .!?/\\]", '',line)
        letter_count = len(line)
output = f'''Paragraph Analysis
-----------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {round(letter_count/word_count,2)}
Average Sentence Length: {word_count/sentence_count}'''
print(output)