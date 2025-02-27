def filter_chars(s):
    to_remove = [chr(i) for i in range(58, 87)]
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)