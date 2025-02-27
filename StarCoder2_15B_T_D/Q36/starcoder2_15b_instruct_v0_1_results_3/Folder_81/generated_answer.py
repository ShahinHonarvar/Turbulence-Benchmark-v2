def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('6'), ord('f') + 1)))
    result = []
    for char in string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)