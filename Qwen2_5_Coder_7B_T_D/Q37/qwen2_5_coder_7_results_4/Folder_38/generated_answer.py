def filter_chars(s):
    chars_to_remove = set('abcdef')
    result = []
    for i, char in enumerate(s):
        if i < 24 or i > 79 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)