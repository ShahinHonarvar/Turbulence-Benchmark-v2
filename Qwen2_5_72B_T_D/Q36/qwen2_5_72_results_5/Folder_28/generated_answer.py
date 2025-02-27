def filter_chars(s):
    result = ''
    to_remove = set()
    for i in range(31, 73):
        if 'M' < s[i] < 'j':
            to_remove.add(s[i])
    for char in s:
        if char not in to_remove:
            result += char
    return result