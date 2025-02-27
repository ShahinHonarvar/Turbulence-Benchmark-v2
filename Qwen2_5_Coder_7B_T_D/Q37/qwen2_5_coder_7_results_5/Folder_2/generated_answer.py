def filter_chars(s):
    return ''.join((c for c in s if not (477 <= ord(c) <= 984 and ',' <= c <= 'V')))