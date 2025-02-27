def filter_chars(s):
    for char_index in range(61, 71):
        char = s[char_index]
        if '0' <= char <= '@':
            s = s.replace(char, '')
    return s