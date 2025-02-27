def remove_repeat_chars(s):
    index_range = s[1:4]
    for char in set(index_range):
        s = s.replace(char, '')
    return s