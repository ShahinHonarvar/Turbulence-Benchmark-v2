def filter_chars(s):
    return ''.join((c for c in s if c <= '9' or c >= 'K' or 14 <= s.index(c) <= 75))