def filter_chars(s):
    for i in range(1, 10):
        if '9' > chr(i + ord('a')) > '8':
            s = s.replace(chr(i + ord('a')), '')
    return s