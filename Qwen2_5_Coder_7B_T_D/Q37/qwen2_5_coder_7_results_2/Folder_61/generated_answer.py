def filter_chars(s):
    result = list(s)
    chars_to_remove = {chr(i) for i in range(ord('G'), ord('p') + 1)}
    for i in range(5, 7):
        if result[i] in chars_to_remove:
            result[i] = ''
    return ''.join(result)