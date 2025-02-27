def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('-'), ord('n') + 1)))
    result = []
    for i, char in enumerate(s):
        if 29 <= i <= 97 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)