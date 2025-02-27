def filter_chars(s):
    chars_to_remove = set()
    for i in range(82, 93):
        char = chr(i)
        if '!' < char < '*':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)