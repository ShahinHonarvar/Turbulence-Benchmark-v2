def filter_chars(s):
    result = []
    to_remove = set()
    for i in range(31, 70):
        if 'B' < s[i] < 'v':
            to_remove.add(s[i])
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)