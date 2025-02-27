def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('l') + 1, ord('t'))]
    result = []
    for char in s:
        if char not in char_to_remove:
            result.append(char)
    return ''.join(result)