def filter_chars(s):
    filtered = ''
    for char in s:
        char_val = ord(char)
        if 71 <= char_val <= 96 and '_' <= char <= 'o':
            continue
        filtered += char
    return filtered