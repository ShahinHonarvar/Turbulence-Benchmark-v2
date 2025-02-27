def filter_chars(s):
    result = []
    for char in s:
        if ord('m') < ord(char) < ord('w'):
            continue
        result.append(char)
    return ''.join(result)