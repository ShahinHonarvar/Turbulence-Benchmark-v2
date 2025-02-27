from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 81:
        return s
    sub = s[38:81]
    counts = Counter(sub)
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))