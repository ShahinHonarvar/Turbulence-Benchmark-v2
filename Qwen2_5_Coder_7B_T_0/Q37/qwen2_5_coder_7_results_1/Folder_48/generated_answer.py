def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (513 <= i <= 877 and '?' <= c <= 'n')))