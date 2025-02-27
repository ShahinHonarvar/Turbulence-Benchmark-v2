def filter_chars(s):
    to_remove = set()
    for i in range(75, 100):
        char = s[i]
        if '8' <= char <= 'e':
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)