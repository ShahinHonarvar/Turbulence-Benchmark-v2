def filter_chars(s):
    for i in range(164, 707):
        if 16 <= i <= 125:
            char = chr(i)
            if 'O' <= char <= '}':
                s = s.replace(char, '')
    return s