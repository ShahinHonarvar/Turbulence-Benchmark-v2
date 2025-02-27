def filter_chars(s):
    result = list(s)
    chars_to_remove = set()
    for i in range(3, 9):
        if '*' < s[i] < 'E':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        result = [c for c in result if c != char]
    return ''.join(result)