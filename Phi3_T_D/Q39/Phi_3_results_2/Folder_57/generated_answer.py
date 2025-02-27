def return_n_greatest_chars(s):
    desired_length = 29
    sorted_chars = sorted(s, reverse=True)
    return sorted_chars[:desired_length]