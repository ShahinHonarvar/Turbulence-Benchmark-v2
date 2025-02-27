def filter_chars(s):
    return ''.join([ch for ch in s if not (46 < ord(ch) < 91 and 'D' < ch < 'H')])