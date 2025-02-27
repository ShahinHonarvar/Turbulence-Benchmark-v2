def filter_chars(s):
    to_remove = set()
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)