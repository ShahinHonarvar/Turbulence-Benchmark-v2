def filter_chars(s):
    c, n = (ord('c'), ord('n'))
    altered_s = [char for index, char in enumerate(s) if not (c <= ord(char) <= n and 13 <= index <= 28)]
    return ''.join(altered_s)