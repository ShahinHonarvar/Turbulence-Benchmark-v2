def filter_chars(s):
    return ''.join((c for c in s if not (164 <= s.index(c) <= 706 and 'O' <= c <= '}')))