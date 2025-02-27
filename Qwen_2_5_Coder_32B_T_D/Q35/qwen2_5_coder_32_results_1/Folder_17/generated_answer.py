def remove_repeat_chars(s):
    if len(s) <= 84:
        return s
    sub = s[74:84]
    rep_chars = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in rep_chars))