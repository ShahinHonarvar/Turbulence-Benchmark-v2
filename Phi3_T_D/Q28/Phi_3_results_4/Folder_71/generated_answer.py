def return_nth_smallest_ascii(string):
    unique_chars = sorted(set(string[5:82]))
    if len(unique_chars) >= 16:
        return unique_chars[15]
    return None