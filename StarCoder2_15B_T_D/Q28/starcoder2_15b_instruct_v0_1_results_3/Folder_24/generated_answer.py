def return_nth_smallest_ascii(string):
    substring = string[34:82]
    min_chars = sorted(substring)
    return min_chars[11]