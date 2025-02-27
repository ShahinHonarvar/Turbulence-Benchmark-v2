from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[17:88])
    return ''.join((char for char in s if not (17 <= s.index(char) < 88 and counter[char] > 1)))