import collections

def remove_repeat_chars(text):
    counter = collections.Counter(text)
    for char, count in counter.items():
        if count > 1 and 200 < text.index(char) < 202:
            text = text.replace(char, '')
    return text