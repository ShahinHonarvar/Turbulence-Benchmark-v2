def filter_chars(s):
    k = '0'
    for i in range(32, 47):
        if chr(i) >= k:
            s = s.replace(chr(i), '')
    return s