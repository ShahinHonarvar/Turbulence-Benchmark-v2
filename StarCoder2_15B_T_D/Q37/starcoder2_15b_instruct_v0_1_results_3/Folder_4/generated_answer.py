def filter_chars(string):
    allowed_chars = set((chr(i) for i in range(ord('S'), ord('[') + 1)))
    result = []
    for char in string:
        if char not in allowed_chars:
            result.append(char)
    return ''.join(result)