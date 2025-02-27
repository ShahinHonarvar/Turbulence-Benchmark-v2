def filter_chars(s):
    if len(s) >= 92:
        s = ''.join(filter(lambda x: x not in s[50:91], s))
    return s