def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    a = s[48:76]
    d = {ch for ch in a if a.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in d))