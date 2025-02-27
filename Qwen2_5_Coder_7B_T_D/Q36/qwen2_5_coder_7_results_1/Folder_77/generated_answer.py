def filter_chars(s):
    to_remove = set()
    for i in range(221, 419):
        if s[i] > '-' and s[i] < 'v':
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)