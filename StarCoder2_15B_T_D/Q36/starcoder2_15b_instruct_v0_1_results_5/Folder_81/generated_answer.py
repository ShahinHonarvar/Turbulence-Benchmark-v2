def filter_chars(s: str) -> str:
    """
    Removes all occurrences of characters between indices 51 and 76 (both exclusive) in the given string's'
    if that character is greater than '5' and smaller than 'f'.
    """
    chars_to_remove = set((chr(i) for i in range(ord('5') + 1, ord('f'))))
    result = []
    for i, c in enumerate(s):
        if i >= 51 and i < 76 and (c in chars_to_remove):
            continue
        result.append(c)
    return ''.join(result)