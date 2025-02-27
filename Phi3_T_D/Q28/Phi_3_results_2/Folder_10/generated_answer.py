def return_nth_smallest_ascii(text):
    filtered_chars = [char for char in text[38:83] if text.count(char) == 1]
    if len(filtered_chars) < 20:
        return None
    return sorted(filtered_chars, key=ord)[19]