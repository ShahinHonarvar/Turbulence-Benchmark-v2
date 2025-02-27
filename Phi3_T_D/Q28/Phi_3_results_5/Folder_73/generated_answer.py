def return_nth_smallest_ascii(s):
    char_list = [s[i] for i in range(70)]
    char_list.sort(key=ord)
    return char_list[9]