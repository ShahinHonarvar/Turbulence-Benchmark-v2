def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if (i < 770 or i > 970) or not '-' <= c <= 'D'])