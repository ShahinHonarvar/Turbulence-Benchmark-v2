def filter_chars(s):
    return ''.join((c for c in s if not (71 <= s.find(c) <= 96 and '_' <= c <= 'o')))