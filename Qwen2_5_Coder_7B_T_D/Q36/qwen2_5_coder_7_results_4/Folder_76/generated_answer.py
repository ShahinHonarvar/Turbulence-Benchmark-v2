def filter_chars(s):
    char_range = set('CDEFGHIJKLMNPQRSTUVWXYZ')
    result = []
    for i, char in enumerate(s):
        if i not in range(669, 888):
            result.append(char)
        elif char in char_range:
            s = s.replace(char, '')
    return s