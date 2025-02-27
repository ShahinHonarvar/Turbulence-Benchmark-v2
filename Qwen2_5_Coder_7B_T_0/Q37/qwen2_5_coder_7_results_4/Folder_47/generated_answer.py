def filter_chars(s):
    chars_to_remove = set(':";<=>?@[\\\\]^_`{|}~')
    result = []
    for i, char in enumerate(s):
        if 38 <= i <= 54 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)