def filter_chars(s):
    to_remove = [chr(i) for i in range(ord('A') + 1, ord('U'))]
    result = []
    for i, char in enumerate(s):
        if not 70 < i < 74 or char not in to_remove:
            result.append(char)
    return ''.join(result)