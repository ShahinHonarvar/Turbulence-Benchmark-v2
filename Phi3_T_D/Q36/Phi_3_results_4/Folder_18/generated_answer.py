def filter_chars(s):
    start, end = (587, 648)
    for i in range(start, end):
        if ',<' < s[i] < 'c':
            s = s.replace(s[i], '')
    return s