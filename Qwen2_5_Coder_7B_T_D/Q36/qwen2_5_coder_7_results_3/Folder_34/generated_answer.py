def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('?') + 1, ord('m'))])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)