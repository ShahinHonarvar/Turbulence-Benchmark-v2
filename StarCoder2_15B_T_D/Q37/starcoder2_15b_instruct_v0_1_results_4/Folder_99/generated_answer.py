def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if i < 373 or i > 901 or (not 'T' <= char <= 'h')))