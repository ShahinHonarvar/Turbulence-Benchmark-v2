def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+{}|:"<>?`~')
    result = list(s)
    for i in range(27, 86):
        if result[i] in chars_to_remove:
            result[i] = ''
    return ''.join(result)