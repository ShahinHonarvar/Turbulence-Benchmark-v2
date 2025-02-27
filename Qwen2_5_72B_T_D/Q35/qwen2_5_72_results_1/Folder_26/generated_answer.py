from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 68:
        return s
    part = s[68:100]
    counter = Counter(part)
    to_remove = {char for char, count in counter.items() if count > 1}
    result = [char for char in s if char not in to_remove]
    return ''.join(result)