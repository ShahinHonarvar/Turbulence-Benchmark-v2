def filter_chars(s):
    valid_chars = [chr(i) for i in range(ord('&'), ord('v') + 1)]
    return ''.join([char for i, char in enumerate(s) if i < 12 or i > 87 or char not in valid_chars])