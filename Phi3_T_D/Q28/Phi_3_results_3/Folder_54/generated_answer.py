def return_nth_smallest_ascii(text):
    sliced_chars = text[12:88]
    filtered_chars = sorted(sliced_chars)
    try:
        return filtered_chars[16]
    except IndexError:
        return None