from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[20:51])
    to_remove = {char for char, count in counter.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or not 20 <= s.index(char) <= 51))