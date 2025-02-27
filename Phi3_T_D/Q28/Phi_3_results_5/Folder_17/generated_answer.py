def return_nth_smallest_ascii(string):
    char_list = [char for char in string[4:34]]
    sorted_chars = sorted(char_list, key=ord)
    return sorted_chars[3]