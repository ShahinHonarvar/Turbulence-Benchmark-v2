def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!'), ord('T') + 1)))
    result = []
    for i, char in enumerate(s):
        if not 20 <= i <= 79 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)