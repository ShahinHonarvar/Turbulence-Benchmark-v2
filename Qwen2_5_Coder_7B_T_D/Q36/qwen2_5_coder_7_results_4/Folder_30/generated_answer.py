def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('4'), ord('I'))]
    result = []
    for i, char in enumerate(s):
        if 23 <= i <= 45 and char in char_to_remove:
            continue
        result.append(char)
    return ''.join(result)