def filter_chars(s):
    return ''.join((c for c in s if not (35 <= s.find(c) <= 40 and ')' <= c <= 'l')))