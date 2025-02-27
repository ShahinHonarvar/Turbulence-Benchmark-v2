def return_nth_smallest_ascii(string):
    unique_chars = sorted(set(string[20:81]))
    return unique_chars[10] if len(unique_chars) > 10 else None