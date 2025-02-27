def filter_chars(s):
    to_remove = set()
    for i in range(40, 63):
        char = s[i]
        if char > '7' and char < 'H':
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)