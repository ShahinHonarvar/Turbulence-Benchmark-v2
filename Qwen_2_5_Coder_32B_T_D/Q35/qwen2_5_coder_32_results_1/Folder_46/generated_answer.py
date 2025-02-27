def remove_repeat_chars(s):
    t = s[10:80]
    rep_chars = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in rep_chars))