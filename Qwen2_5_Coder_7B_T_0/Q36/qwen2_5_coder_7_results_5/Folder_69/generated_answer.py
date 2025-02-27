def filter_chars(s):
    chars_to_remove = set()
    for i in range(344, 665):
        char = s[i]
        if '%' < char < 'U':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)