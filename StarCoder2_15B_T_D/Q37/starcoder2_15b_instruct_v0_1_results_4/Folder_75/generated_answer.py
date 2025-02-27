def filter_chars(s):
    indices = range(34, 68)
    chars = list(s)
    for i in indices:
        if chars[i] >= 'W' and chars[i] <= 'x':
            chars.remove(chars[i])
            i -= 1
    return ''.join(chars)