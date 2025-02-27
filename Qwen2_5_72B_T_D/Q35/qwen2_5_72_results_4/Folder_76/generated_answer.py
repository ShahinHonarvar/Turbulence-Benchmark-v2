from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[330:543])
    repeats = {char for char, count in counter.items() if count > 1}
    return ''.join((char for char in s if char not in repeats or not 330 <= s.index(char) < 543))