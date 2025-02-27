def filter_chars(s):
    chars_to_remove = set('abcdefghij')
    result = []
    for i, char in enumerate(s):
        if not 83 <= i <= 99 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)