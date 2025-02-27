def filter_chars(s):
    to_remove = set()
    for i in range(14, 75):
        if '9' < s[i] < 'K':
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)