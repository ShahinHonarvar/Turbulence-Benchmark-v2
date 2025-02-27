def filter_chars(s):
    start, end = (722, 832)
    for i in range(start, end + 1):
        if 'K' <= s[i] <= 'm':
            s = s.replace(s[i], '')
    return s