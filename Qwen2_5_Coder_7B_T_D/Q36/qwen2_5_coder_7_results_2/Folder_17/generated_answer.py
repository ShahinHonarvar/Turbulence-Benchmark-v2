def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(76, 97)]
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)