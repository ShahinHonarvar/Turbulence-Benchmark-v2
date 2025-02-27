def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    t = s[87:99]
    d = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in d))