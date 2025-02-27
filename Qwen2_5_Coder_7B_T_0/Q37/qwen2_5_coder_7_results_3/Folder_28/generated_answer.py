def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+{}|:"<>?')
    result = []
    for i, char in enumerate(s):
        if 20 <= i <= 79 and char not in chars_to_remove:
            result.append(char)
    return ''.join(result)