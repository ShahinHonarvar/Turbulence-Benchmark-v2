def filter_chars(s):
    return ''.join((ch for ch in s if not '!' < ch < 'A'))