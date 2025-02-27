def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not 'ff' <= char <= 'u' or not 31 <= i < 70])