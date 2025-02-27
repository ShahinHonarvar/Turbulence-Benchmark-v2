def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(62, 95)))
    result = []
    for i, char in enumerate(s):
        if i < 521 or i > 722 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)