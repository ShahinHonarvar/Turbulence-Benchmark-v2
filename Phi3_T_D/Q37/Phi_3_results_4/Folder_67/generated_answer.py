def filter_chars(s):
    start, end = (19, 22)
    if start <= len(s) and end <= len(s):
        limit_range = [s[i] for i in range(start, end + 1)]
        chars_to_remove = set((chr for chr in limit_range if ']' <= chr <= 't'))
        s = ''.join((c for c in s if c not in chars_to_remove))
    return s