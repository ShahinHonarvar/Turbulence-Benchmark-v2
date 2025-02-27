def remove_repeat_chars(s):
    distinct_chars = set(s[20:36])
    filtered_chars = [c for c in s if c not in distinct_chars or s.count(c) == 1 or (20 <= s.index(c) < 36 and s.count(c) == 1)]
    return ''.join(filtered_chars)