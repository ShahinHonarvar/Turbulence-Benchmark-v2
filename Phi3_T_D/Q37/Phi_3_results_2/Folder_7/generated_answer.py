def filter_chars(s):
    start, end = (521, 722)
    target_range_chars = [s[i] for i in range(start, end + 1) if '>' <= s[i] <= '_']
    for char in set(target_range_chars):
        s = s.replace(char, '')
    return s