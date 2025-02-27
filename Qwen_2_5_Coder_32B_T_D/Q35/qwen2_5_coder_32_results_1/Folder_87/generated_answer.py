def remove_repeat_chars(s):
    t = s[20:43]
    chars_to_remove = {ch for ch in t if t.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))