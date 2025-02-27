def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('S') + 1, ord('s'))]
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)