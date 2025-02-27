def filter_chars(text):
    return ''.join((c for c in text if c < '@' or c > 'p' or (c < 'G' and c > '68')))