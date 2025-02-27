def return_n_smallest_chars(string):
    chars_sorted = sorted(string)
    top_35_smallest = chars_sorted[:min(35, len(string))]
    return top_35_smallest[::-1]