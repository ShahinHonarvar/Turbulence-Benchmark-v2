def filter_chars(s):
    start, end = (23, 83)
    chars_to_filter = [chr(i) for i in range(ord('f') + 1, ord('o'))]
    result = []
    for index, char in enumerate(s):
        if start < index < end and char in chars_to_filter:
            continue
        result.append(char)
    return ''.join(result)