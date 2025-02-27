def filter_chars(s):
    to_remove = set()
    for i in range(55, 84):
        char = chr(i)
        if ';' < char < 'z':
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)