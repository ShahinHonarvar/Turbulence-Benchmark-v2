from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[20:51])
    return ''.join((char for char in s if not (20 <= s.index(char) <= 51 and counter[char] > 1)))