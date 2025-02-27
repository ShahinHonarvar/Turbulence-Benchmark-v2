def return_nth_smallest_ascii(text):
    unique_chars = sorted(set(text[18:46]))
    if len(unique_chars) >= 7:
        return unique_chars[6]
    return None