def filter_chars(s):
    start, end = (35, 89)
    for char in set([s[i] for i in range(start, end + 1) if 'E' <= s[i] <= 't']):
        s = s.replace(char, '')
    return s