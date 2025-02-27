def filter_chars(s):
    start, end = (min(34, len(s)), min(67, len(s)))
    to_remove = ''.join((ch for ch in s[start:end + 1] if 'W' <= ch <= 'x'))
    result = s.replace(to_remove, '')
    return result