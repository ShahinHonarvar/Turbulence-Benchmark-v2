def remove_repeat_chars(s):
    c = s[200:202]
    for ch in set(c):
        s = s.replace(ch, '')
    return s