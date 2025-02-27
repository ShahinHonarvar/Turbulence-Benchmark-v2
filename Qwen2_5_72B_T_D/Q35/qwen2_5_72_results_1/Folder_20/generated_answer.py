from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[27:96])
    repeats = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeats or not 27 <= s.index(char) < 96))
    return result