def return_nth_smallest_ascii(s):
    substring = s[:88]
    sorted_chars = sorted(substring)
    return sorted_chars[13]