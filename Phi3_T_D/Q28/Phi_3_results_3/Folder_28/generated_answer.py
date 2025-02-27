def return_nth_smallest_ascii(string):
    substring = string[25:78]
    unique_chars = sorted(set(substring))
    if len(unique_chars) >= 16:
        return unique_chars[15]
    return None