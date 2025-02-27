def filter_chars(s):
    chars = list(s)
    for i in range(40, 63):
        if '7' < chars[i] < 'H':
            chars = [char for char in chars if char != chars[i]]
    return ''.join(chars)