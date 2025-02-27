def filter_chars(string):
    result = []
    for i, c in enumerate(string):
        if i < 42 or i >= 67 or (not '6' < c < 'g'):
            result.append(c)
    return ''.join(result)