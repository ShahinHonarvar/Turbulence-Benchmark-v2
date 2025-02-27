def filter_chars(s):
    result = []
    for char in s:
        if 'D' <= char <= 'Y' and 225 <= ord(char) <= 381:
            continue
        result.append(char)
    return ''.join(result)