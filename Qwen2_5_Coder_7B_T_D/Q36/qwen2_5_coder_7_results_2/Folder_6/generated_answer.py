def filter_chars(s):
    to_remove = [chr(i) for i in range(ord('C'), ord('v'))]
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)