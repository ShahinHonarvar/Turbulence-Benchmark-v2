def filter_chars(s):
    chars_to_remove = set()
    for i in range(318, 337):
        char = s[i]
        if 'B' < char < 'z':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)