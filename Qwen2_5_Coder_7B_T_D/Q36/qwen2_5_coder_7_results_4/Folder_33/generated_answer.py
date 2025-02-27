def filter_chars(s):
    return ''.join((ch for ch in s if not (299 < s.index(ch) < 418 and '9' < ch < 'P')))