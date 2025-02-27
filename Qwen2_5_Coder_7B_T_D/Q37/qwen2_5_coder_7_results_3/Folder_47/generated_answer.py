def filter_chars(s):
    chars_to_remove = set('abcdefghijklmnopqrstuvwxyz0123456789')
    result = []
    for i, char in enumerate(s):
        if 38 <= i <= 54 and char >= ':' and (char <= 'r'):
            chars_to_remove.add(char)
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)