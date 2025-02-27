def filter_chars(s):
    return ''.join((c for c in s if c < '8' or c > 'e' or (not 75 <= ord(c) - ord('0') <= 99)))