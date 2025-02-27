def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 502 < i < 946:
            if 'W' < char < 'y':
                continue
        result.append(char)
    return ''.join(result)