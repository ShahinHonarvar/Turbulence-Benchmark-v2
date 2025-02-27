def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 27 <= i <= 85:
            if ord('c') <= ord(char) <= ord('i'):
                continue
        result.append(char)
    return ''.join(result)