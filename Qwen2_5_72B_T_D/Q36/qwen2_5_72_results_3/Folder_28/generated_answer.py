def filter_chars(s):
    result = []
    chars_to_remove = set()
    for i in range(31, 73):
        if 'M' < s[i] < 'j':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)