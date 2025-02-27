def filter_chars(s):
    if len(s) > 9:
        char_to_filter = s[8:10]
        s = ''.join([c for c in s if not char_to_filter[0] <= c <= char_to_filter[1]])
    return s