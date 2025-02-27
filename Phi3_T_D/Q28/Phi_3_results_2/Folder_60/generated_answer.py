def return_nth_smallest_ascii(string):
    filtered_chars = sorted([char for char in string[36:80] if char not in [' ', '']])
    return filtered_chars[11] if len(filtered_chars) > 11 else None