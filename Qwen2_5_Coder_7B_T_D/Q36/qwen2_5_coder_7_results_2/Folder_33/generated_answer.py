def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A'), ord('P')) if i > ord('9')}
    result = []
    for i, char in enumerate(s):
        if i < 299 or i >= 418 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)