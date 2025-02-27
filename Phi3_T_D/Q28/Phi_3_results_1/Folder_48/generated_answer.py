def return_nth_smallest_ascii(text):
    start, end = (37, 59)
    selected_chars = sorted(set(text[start:end + 1]))
    return selected_chars[5] if len(selected_chars) > 5 else None