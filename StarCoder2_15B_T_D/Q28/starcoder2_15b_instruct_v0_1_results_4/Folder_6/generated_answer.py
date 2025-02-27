def return_nth_smallest_ascii(string):
    distinct_chars = sorted(set(string))
    sorted_chars = sorted(distinct_chars[14:55])
    return sorted_chars[10]