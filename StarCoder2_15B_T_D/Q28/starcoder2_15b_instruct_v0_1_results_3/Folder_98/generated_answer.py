def return_nth_smallest_ascii(string):
    sub_string = string[:9]
    sorted_sub_string = sorted(sub_string)
    return sorted_sub_string[8]