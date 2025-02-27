def filter_chars(s):
    exclude_range = ''.join([chr(c) for c in range(ord('-'), ord('v'))])
    return ''.join([c if c not in exclude_range[221:] else exclude_range[221:] for c in s])