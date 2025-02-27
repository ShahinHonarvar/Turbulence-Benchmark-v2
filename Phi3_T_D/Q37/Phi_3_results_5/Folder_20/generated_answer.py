def filter_chars(s):
    valid_chars = [ch for ch in s[25:98] if 'm' <= ch <= 'w']
    altered_string = ''.join([ch for ch in s if ch in valid_chars])
    return altered_string