def remove_repeat_chars(s):
    chars = s[1:5]
    repeats = {c for c in chars if chars.count(c) > 1}
    return ''.join((c for c in s if c not in repeats))