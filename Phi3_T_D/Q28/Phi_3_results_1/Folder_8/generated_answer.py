def return_nth_smallest_ascii(string):
    target_range = string[60:89]
    nth_smallest = sorted(target_range)[6]
    return nth_smallest