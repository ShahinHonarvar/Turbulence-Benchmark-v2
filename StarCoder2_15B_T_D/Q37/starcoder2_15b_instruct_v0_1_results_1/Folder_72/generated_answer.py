def filter_chars(string):
    return ''.join((c for c in string if c < 'H' or c > 's' or (not 35 <= ord(c) - ord('H') <= 51)))