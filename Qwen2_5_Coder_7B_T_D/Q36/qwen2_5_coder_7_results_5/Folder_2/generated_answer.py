def filter_chars(s):
    if len(s) <= 854:
        return s
    char_to_remove = [chr(i) for i in range(ord('D') + 1, ord('J'))]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s