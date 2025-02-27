def return_nth_smallest_ascii(s):
    sub_str = s[:46]
    return min(set(sub_str), key=lambda x: ord(x))