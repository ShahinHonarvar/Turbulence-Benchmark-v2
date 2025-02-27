def filter_chars(string: str) -> str:
    chars_to_remove = set((chr(c) for c in range(ord('-'), ord('D') + 1)))
    filtered_chars = []
    for index, char in enumerate(string):
        if index < 770 or index > 970 or char not in chars_to_remove:
            filtered_chars.append(char)
    return ''.join(filtered_chars)