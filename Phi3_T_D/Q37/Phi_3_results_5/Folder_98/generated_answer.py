def filter_chars(s):
    char = s[7:10]
    char = ''.join(filter(lambda c: 'R' <= c <= 't', char))
    return s.replace(char, '')