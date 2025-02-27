def filter_chars(s):
    to_remove = set('6789AB')
    result = []
    for i, char in enumerate(s):
        if i < 138 or i > 920 or char not in to_remove:
            result.append(char)
    return ''.join(result)