def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not 38 <= i <= 69 or not 'H' >= c <= 'e'])