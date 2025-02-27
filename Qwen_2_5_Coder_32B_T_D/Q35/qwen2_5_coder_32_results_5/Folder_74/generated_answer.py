def remove_repeat_chars(s):
    t = s[70:97]
    chars = {ch for ch in t if t.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars))