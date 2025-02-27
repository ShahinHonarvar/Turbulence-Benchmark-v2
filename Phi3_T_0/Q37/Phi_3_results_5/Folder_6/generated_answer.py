def filter_chars(s):
    c = 'c'
    n = 'n'
    return ''.join((char for i, char in enumerate(s) if not c <= char <= n or not 13 <= i <= 28))