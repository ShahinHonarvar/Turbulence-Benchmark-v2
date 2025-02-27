def remove_repeat_chars(s):
    chars = set()
    for i in range(36, 52):
        if s[i] in chars:
            s = s.replace(s[i], '')
        else:
            chars.add(s[i])
    return s