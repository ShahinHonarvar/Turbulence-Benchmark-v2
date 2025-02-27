def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('7'), ord('e') + 1)}
    result = list(s)
    for i in range(22, min(86, len(s))):
        if result[i] in chars_to_remove:
            result[i] = ''
    return ''.join(result)