def filter_chars(s):
    to_remove = set()
    for i in range(21, 25):
        char = s[i]
        if '5' < char < '}':
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)