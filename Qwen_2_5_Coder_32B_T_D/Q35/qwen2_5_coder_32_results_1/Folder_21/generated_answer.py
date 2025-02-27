def remove_repeat_chars(s):
    a = s[463:995]
    to_remove = {ch for ch in a if a.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in to_remove))