def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    top_87_chars = sorted_chars[:87]
    return top_87_chars