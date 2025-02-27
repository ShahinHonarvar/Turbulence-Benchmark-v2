def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('i'), ord('v') + 1)]
    result = []
    for i, char in enumerate(s):
        if not 11 <= i <= 72 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)