def filter_chars(s):
    chars_to_remove = set()
    for i in range(300, 418):
        char = s[i]
        if '9' < char < 'P':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)