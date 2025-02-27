def filter_chars(s):
    chars_to_remove = set('0123456789')
    result = []
    for i, char in enumerate(s):
        if 54 <= i <= 62 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)