def return_nth_smallest_ascii(string):
    first_13_chars = string[:13]
    sorted_chars = sorted(first_13_chars)
    return sorted_chars[-1] if len(sorted_chars) == 13 else ''