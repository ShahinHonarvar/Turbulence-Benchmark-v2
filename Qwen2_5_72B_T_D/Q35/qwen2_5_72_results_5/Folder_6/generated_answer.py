from collections import Counter

def remove_repeat_chars(s):
    cnt = Counter(s[20:93])
    return ''.join((c for i, c in enumerate(s) if i < 20 or i >= 93 or cnt[c] < 2))