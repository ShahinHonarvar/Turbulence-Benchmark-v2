from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[13:70])
    return ''.join(('' if 13 <= i < 70 and counter[char] > 1 else char for i, char in enumerate(s)))