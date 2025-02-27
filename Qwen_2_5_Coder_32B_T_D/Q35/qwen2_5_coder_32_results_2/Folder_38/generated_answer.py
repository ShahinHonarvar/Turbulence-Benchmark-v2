def remove_repeat_chars(s):
    if len(s) <= 86:
        return s
    t = s[37:85]
    duplicates = {ch for ch in t if t.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in duplicates))