def filter_chars(string: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord(','), ord('c'))))
    result = []
    for char in string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)