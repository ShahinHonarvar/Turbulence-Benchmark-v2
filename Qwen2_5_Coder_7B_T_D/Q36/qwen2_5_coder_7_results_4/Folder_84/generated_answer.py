def filter_chars(s):
    char_range = 'defghijklmnopqrst'
    result = ''
    for i, char in enumerate(s):
        if i < 171 or i >= 636 or char not in char_range:
            result += char
    return result