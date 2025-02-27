def filter_chars(s):
    chars_to_remove = set(s[70:74])
    result = []
    for char in s:
        if char not in chars_to_remove or char <= 'A' or char >= 'U':
            result.append(char)
    return ''.join(result)