import collections

def remove_repeat_chars(string):
    counter = collections.Counter(string[27:96])
    for char, count in counter.items():
        if count > 1:
            string = string.replace(char, '')
    return string