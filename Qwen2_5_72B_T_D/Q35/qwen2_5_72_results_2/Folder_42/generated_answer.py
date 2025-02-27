from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[18:60])
    return ''.join(('' if 18 <= i < 60 and counter[char] > 1 else char for i, char in enumerate(s)))