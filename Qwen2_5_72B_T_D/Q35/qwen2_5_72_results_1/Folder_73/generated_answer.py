from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[10:76])
    to_remove = {char for char, count in counter.items() if count > 1}
    return ''.join((char for i, char in enumerate(s) if not (10 <= i < 76 and char in to_remove)))