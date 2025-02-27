def filter_chars(s):
    to_remove = set()
    for i in range(35, 52):
        char = s[i]
        if 'H' <= char <= 's':
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)