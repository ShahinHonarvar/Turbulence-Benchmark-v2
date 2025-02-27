def filter_chars(s):
    start, stop = (75, 99)
    rep_chars = '0123456789:;<=>?@ABCDEFGHIJKLMNOP'
    return ''.join([char for i, char in enumerate(s) if not (start <= i <= stop and char in rep_chars)])