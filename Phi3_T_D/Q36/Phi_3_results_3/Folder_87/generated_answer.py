def filter_chars(s):
    result = []
    char_to_remove = ''.join((chr(i) for i in range(49, 65) if chr(i) > '3'))
    for char in s:
        if char not in char_to_remove or ord(char) <= 48 or ord(char) >= 65:
            result.append(char)
    return ''.join(result)