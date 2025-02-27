def return_nth_smallest_ascii(s):
    char_list = sorted([char for char in s[:12]])
    return char_list[11]