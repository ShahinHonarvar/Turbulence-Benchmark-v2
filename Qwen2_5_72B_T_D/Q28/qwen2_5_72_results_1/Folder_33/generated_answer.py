def return_nth_smallest_ascii(s):
    char_list = [s[i] for i in range(22, 75) if s[i] in set(s)]
    char_list_sorted = sorted(char_list, key=ord)
    return char_list_sorted[11]