def filter_chars(s):
    chars_to_remove = set()
    for i in range(43, 69):
        if 'B' < s[i] < 'r':
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result