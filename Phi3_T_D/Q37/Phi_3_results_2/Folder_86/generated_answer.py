def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (164 <= i <= 706 and 'O' <= c <= '}')))