def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (259 <= i <= 502 and ',' <= c <= '3')))