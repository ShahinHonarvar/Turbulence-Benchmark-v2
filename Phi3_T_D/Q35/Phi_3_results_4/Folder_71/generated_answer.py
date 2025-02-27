def remove_repeat_chars(s):
    index_range = s[20:36]
    for c in set(index_range):
        if index_range.count(c) > 1:
            s = s.replace(c, '')
    return s