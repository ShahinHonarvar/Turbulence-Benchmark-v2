def filter_chars(s):
    start, end = (1, 7)
    chars_to_remove = set()
    for char in s[start:end + 1]:
        if 'L' <= char <= 'a':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)