def filter_chars(s):
    for ch in range(ord('57'), ord('97')):
        if chr(ch) >= '<' and chr(ch) <= 'w':
            s = s.replace(chr(ch), '')
    return s