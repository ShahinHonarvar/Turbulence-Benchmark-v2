def filter_chars(s):
    start, end = (331, 713)
    pattern = ''.join((chr(i) for i in range(ord('M') + 1, ord('_')) if i > ord('M')))
    return s.translate(str.maketrans('', '', pattern))