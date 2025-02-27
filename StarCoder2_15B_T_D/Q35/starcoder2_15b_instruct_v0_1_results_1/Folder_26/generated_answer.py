from collections import Counter

def remove_repeat_chars(s: str) -> str:
    counter = Counter(s[68:99])
    for c in counter:
        if counter[c] > 1:
            s = s.replace(c, '')
    return s