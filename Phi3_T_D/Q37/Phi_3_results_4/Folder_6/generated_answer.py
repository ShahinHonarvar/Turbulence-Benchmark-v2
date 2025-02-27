def filter_chars(s):
    start, end = (13, 28)
    c, n = (ord('c'), ord('n'))
    altered_chars = []
    for i, char in enumerate(s):
        if c <= ord(char) <= n and start <= i <= end:
            continue
        altered_chars.append(char)
    return ''.join(altered_chars)