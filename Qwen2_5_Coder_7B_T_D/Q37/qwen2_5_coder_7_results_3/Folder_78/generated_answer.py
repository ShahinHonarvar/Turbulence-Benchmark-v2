def filter_chars(s):
    chars = list(s)
    for i in range(75, 100):
        if '8' <= chars[i] <= 'e':
            chars[i] = ''
    return ''.join(chars)