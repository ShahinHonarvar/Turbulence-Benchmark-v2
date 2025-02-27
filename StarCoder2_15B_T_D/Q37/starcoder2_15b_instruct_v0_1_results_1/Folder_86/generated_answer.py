def filter_chars(text: str) -> str:
    start_index = 164
    end_index = 706
    char_range = range(ord('O'), ord('}') + 1)
    filtered_chars = [c for i, c in enumerate(text) if i < start_index or i > end_index or ord(c) not in char_range]
    filtered_text = ''.join(filtered_chars)
    return filtered_text