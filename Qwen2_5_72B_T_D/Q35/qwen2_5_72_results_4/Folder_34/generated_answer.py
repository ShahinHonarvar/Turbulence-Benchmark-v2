from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[70:200])
    repeat_chars = {char for char, count in counter.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or not 70 <= s.index(char) < 200))
    return result