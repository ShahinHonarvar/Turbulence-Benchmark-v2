def return_nth_smallest_ascii(text):
    chars_in_range = [char for index, char in enumerate(text) if 50 <= index <= 76]
    sorted_chars = sorted(chars_in_range, key=ord)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None