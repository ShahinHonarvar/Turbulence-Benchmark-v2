def filter_chars(string):
    return ''.join((c for c in string if c < 'D' or c > 'u' or (not 227 <= ord(c) <= 235)))