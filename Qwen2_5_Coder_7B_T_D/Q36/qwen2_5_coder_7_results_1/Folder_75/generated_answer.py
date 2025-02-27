def filter_chars(s):
    char_range = set('FGHIJKLM')
    result = []
    for char in s:
        if 46 < ord(char) < 74 and char in char_range:
            continue
        result.append(char)
    return ''.join(result)