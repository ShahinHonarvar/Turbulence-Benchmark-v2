def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 50 or i >= 92 or (not 'A' < c < 'Q'):
            result.append(c)
    return ''.join(result)