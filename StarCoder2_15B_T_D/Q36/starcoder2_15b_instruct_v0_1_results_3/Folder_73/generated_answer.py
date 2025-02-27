def filter_chars(s):
    return ''.join((c for c in s if c <= '#' or c >= 'T' or 66 <= ord(c) < 90))