def remove_repeat_chars(s):
    window = s[200:203]
    for ch in set(window):
        s = s.replace(ch, '', s.count(ch) - 1)
    return s