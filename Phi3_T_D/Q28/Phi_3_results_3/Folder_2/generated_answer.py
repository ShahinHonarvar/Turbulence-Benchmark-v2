def return_nth_smallest_ascii(string):
    target_chars = string[48:77]
    nth_smallest = sorted(target_chars)[4]
    return nth_smallest