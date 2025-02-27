def filter_chars(s):
    return ''.join((char for i, char in enumerate(s) if not (40 < i < 63 and '8' > char > 'H')))