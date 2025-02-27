def filter_chars(s):
    result = list(s)
    chars_to_remove = set()
    for i in range(221, 419):
        if 221 <= i < len(s) and '-' < s[i] < 'v':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        result = [c for c in result if c != char]
    return ''.join(result)