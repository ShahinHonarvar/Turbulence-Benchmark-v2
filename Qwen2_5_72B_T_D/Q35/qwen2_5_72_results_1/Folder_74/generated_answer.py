from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[69:97])
    to_remove = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for i, char in enumerate(s) if i < 69 or i >= 97 or char not in to_remove))
    return result