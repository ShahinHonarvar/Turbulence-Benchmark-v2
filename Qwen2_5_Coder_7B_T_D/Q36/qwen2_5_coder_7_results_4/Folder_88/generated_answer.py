def filter_chars(s):
    target_chars = 'TUVWXYZ'
    result = ''
    for char in s:
        if char not in target_chars:
            result += char
    return result