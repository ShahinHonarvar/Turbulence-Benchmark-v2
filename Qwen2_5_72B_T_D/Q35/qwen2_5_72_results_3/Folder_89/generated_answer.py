from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[55:84])
    repeat_chars = {char for char, count in counter.items() if count > 1}
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)