def return_nth_smallest_ascii(string):
    target_range = string[22:75]
    unique_chars = sorted(set(target_range))
    if len(unique_chars) >= 12:
        return unique_chars[11]
    return None