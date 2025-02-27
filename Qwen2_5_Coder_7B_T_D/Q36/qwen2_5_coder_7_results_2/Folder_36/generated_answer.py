def filter_chars(s):
    char_to_remove = set()
    for i in range(283, 484):
        if 'l' < s[i] < 't':
            char_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in char_to_remove:
            result.append(char)
    return ''.join(result)