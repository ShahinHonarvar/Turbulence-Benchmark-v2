def filter_chars(s):
    for i in range(54, 63):
        if ord(')') <= ord(s[i]) <= ord('9'):
            s = s.replace(s[i], '')
    return s