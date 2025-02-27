def return_nth_smallest_ascii(s):
    return min(s[:5], key=ord)