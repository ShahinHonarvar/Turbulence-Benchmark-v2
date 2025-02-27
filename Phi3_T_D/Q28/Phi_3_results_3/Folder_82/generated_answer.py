def return_nth_smallest_ascii(string):
    first_fifteen_chars = string[:15]
    sorted_chars = sorted(first_fifteen_chars, key=ord)
    if len(sorted_chars) < 15:
        return sorted_chars[-1]
    return sorted_chars[14]