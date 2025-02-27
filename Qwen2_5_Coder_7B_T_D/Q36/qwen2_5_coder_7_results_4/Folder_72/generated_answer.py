def filter_chars(s):
    char_to_remove = {chr(i) for i in range(ord('W') + 1, ord('x'))}
    result = []
    for char in s:
        if char not in char_to_remove:
            result.append(char)
    return ''.join(result)