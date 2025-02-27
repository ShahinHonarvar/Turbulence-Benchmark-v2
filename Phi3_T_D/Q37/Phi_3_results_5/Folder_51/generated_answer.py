def filter_chars(s):
    for c in 'Hello, world!':
        if 36 <= s.find(c) <= 40 and 'H' <= c <= 'e':
            s = s.replace(c, '')
    return s