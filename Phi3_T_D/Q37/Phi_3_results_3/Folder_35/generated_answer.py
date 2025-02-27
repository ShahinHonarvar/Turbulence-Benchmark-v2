def filter_chars(s):
    char_range = [ord('('), ord(']')]
    result = []
    for i, c in enumerate(s):
        if 155 <= i <= 403 and char_range[0] <= ord(c) <= char_range[1]:
            continue
        result.append(c)
    return ''.join(result)