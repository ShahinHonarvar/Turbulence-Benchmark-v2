def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('&') + 1, ord('M'))))
    result = []
    for char in string:
        if not (46 < ord(char) < 74 and char in chars_to_remove):
            result.append(char)
    return ''.join(result)