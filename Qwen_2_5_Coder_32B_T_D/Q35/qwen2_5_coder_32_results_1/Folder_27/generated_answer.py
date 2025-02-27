def remove_repeat_chars(s):
    if len(s) <= 89:
        return s
    sub = s[87:89]
    chars_to_remove = {ch for ch in sub if sub.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))