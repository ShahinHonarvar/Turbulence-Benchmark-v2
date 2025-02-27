def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 19 <= i <= 90 or not 'F' <= c <= 'h'))