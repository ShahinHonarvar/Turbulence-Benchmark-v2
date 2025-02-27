def filter_chars(s):
    chars_to_remove = set()
    for i in range(35, 99):
        if 'A' <= s[i] <= 'b':
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result