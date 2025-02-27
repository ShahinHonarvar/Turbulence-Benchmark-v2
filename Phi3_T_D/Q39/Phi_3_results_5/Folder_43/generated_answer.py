def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    top_fifty_six = sorted_chars[:56]
    return top_fifty_six