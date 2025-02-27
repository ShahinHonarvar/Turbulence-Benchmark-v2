from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[103:802])
    to_remove = {char for char, count in counter.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or not 103 <= s.index(char) < 802))