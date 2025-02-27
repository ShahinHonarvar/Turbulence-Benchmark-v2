from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[22:24])
    return ''.join((char for char in s if not (22 <= s.index(char) <= 24 and counter[char] > 1)))