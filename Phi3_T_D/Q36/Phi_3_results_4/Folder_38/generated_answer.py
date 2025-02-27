def filter_chars(s):
    start, end = (44, 48)
    chars_to_filter = set(s[start:end]) - set(['+', 'l'])
    altered_string = ''.join((c for c in s if c not in chars_to_filter or not start < s.index(c) < end))
    return altered_string