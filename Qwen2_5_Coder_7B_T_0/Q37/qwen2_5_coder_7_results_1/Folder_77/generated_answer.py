def filter_chars(s):
    chars_to_remove = set('012345678')
    result = []
    for i, char in enumerate(s):
        if 384 <= i <= 411 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)