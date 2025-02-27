def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('i'), ord('k'))]
    result = []
    for i, char in enumerate(s):
        if not (2 < i < 7 and char in char_to_remove):
            result.append(char)
    return ''.join(result)