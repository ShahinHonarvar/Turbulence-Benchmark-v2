def filter_chars(s):
    return ''.join([ch for ch in s if not (124 <= ord(ch) <= 854 and '9' <= ch <= 's')])