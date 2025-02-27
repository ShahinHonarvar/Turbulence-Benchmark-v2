def filter_chars(text):
    result = []
    for i, c in enumerate(text):
        if i < 38 or i >= 81 or (not '.' < c < '^'):
            result.append(c)
    return ''.join(result)