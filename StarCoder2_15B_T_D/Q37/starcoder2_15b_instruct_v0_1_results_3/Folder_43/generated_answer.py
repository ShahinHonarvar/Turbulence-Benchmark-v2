def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('W'), ord('{') + 1)))
    result = []
    for char in string:
        if char not in chars_to_remove or string.index(char) < 15 or string.index(char) > 55:
            result.append(char)
    return ''.join(result)