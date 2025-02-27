def remove_repeat_chars(s):
    unique_chars = set(s[:5])
    for c in unique_chars:
        if s.count(c) > 1:
            s = s.replace(c, '')
    return s