from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[57:85])
    repeated_chars = {char for char, count in counter.items() if count > 1}
    return ''.join((char for i, char in enumerate(s) if not (57 <= i < 85 and char in repeated_chars)))