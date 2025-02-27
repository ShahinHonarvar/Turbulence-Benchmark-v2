def filter_chars(s, i, k):
    return ''.join((c for index, c in enumerate(s) if index < 20 or not (i <= c <= k and 20 <= index <= 62)))