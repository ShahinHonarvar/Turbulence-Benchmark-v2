def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not (35 <= i <= 40 and ')' <= char <= 'l')])