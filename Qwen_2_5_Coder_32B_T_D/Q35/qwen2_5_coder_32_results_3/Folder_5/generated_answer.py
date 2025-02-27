def remove_repeat_chars(s):
    sub = s[3:8]
    repeats = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in repeats))