def filter_chars(text):
    result = ''
    for i, c in enumerate(text):
        if not (63 <= i <= 84 and 'E' <= c <= '~'):
            result += c
    return result