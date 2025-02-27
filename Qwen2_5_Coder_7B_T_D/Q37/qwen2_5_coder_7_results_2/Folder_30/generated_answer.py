def filter_chars(s):
    chars = list(s)
    for i in range(41, 65):
        if 'K' <= chars[i] <= ']':
            chars = [char for char in chars if char != chars[i]]
    return ''.join(chars)