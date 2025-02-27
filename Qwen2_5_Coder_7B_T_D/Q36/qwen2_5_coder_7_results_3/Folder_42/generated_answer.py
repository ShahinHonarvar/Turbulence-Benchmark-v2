def filter_chars(s):
    target_chars = set('uvw')
    result = ''
    for char in s:
        if 42 < s.index(char) < 68 and char in target_chars:
            continue
        result += char
    return result