def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('('), ord('[') + 1)])
    result = []
    for i, char in enumerate(s):
        if not (155 <= i <= 403 and char in chars_to_remove):
            result.append(char)
    return ''.join(result)