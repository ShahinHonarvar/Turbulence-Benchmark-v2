def return_nth_smallest_ascii(s):
    char_list = [s[i] for i in range(5, 90)]
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[12]