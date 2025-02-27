from collections import Counter

def remove_repeat_chars(s):
    count = Counter(s[29:53])
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove or not 29 <= s.index(char) < 53))