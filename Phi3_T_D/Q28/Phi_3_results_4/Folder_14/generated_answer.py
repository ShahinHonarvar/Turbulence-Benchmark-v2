def return_nth_smallest_ascii(text: str) -> str:
    target_chars = text[46:83]
    valid_chars = {char for char in target_chars if text.count(char) == 1}
    sorted_chars = sorted(valid_chars, key=ord)
    return sorted_chars[15]