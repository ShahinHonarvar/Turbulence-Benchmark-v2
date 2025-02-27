def filter_chars(s):
    return ''.join((c for c in s if c <= 'D' or c >= 'H' or c not in s[46:91]))