def filter_chars(s):
    return ''.join((c for c in s if not (124 <= s.find(c) <= 854 and '9' <= c <= 's')))