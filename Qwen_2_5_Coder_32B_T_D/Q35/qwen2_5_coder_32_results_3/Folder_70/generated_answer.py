def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    substring = s[44:70]
    repeat_chars = {c for c in substring if substring.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))