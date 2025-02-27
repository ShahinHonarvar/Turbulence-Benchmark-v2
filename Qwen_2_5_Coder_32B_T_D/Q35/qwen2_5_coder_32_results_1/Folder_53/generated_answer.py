def remove_repeat_chars(s):
    if len(s) <= 202:
        return s
    sub = s[201:202]
    chars_to_remove = {ch for ch in sub if sub.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))