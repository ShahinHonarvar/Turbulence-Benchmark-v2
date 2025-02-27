def filter_chars(s):
    for i in range(384, 412):
        if 97 <= ord(s[i]) <= 56:
            s = s.replace(s[i], '')
    return s