def filter_chars(s):
    return ''.join((c for c in s if not (63 <= ord(c) <= 84 and 'E' <= c <= '~')))