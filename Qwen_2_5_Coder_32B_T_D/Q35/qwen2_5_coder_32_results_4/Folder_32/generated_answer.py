def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    sub = s[87:90]
    chars = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in chars))