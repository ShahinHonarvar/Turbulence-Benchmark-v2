def remove_repeat_chars(s):
    unique_chars = set()
    for i, c in enumerate(s):
        if i >= 33 and i < 78 and (c in unique_chars):
            s = s.replace(c, '', 1)
        else:
            unique_chars.add(c)
    return s