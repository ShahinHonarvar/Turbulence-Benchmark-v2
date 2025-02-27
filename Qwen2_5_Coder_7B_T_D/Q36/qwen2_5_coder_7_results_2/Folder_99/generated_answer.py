def filter_chars(s):
    target_chars = 'cd'
    result = ''
    for char in s:
        if ord(char) not in range(ord('b') + 1, ord('d')):
            result += char
    return result