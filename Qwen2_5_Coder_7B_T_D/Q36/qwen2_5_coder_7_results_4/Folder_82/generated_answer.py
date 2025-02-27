def filter_chars(s):
    return s[:69] + ''.join((c for c in s[69:97] if c <= 'V' or c >= 'j')) + s[97:]