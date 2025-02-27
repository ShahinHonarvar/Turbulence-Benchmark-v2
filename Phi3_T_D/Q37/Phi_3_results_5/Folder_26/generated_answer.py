def filter_chars(s, i, k):
    for char in set(s[20:63]):
        if i <= char <= k:
            s = s.replace(char, '')
    return s