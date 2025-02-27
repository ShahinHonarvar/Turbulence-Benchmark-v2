import collections

def remove_repeat_chars(string: str) -> str:
    counter = collections.Counter(string[1:7])
    for char, count in counter.items():
        if count > 1:
            string = string.replace(char, '')
    return string