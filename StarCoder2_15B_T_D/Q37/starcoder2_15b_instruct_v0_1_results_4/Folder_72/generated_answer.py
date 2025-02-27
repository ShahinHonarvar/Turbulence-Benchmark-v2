def filter_chars(string):
    filtered = [c for c in string if c < 'H' or c > 's' or 35 > string.index(c) or (string.index(c) > 51)]
    return ''.join(filtered)