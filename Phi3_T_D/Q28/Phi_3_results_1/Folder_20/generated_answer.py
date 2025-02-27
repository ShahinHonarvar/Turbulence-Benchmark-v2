def return_nth_smallest_ascii(s):
    char_list = sorted([s[i] for i in range(25, 65)])
    return char_list[5]