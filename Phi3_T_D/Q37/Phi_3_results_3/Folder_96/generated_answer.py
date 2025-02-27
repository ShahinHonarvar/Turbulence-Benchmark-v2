def filter_chars(s):
    allowed_chars = set('!bcdefghijklmnopqrst')
    return ''.join((c for i, c in enumerate(s) if (i < 86 or i > 92) or c in allowed_chars))