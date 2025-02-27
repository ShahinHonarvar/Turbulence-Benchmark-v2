def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('.'), ord('b') + 1)]
    result = []
    for i, char in enumerate(s):
        if 72 <= i <= 94 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)