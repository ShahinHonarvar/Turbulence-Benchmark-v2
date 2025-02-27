def return_n_greatest_chars(s):
    combined_chars = ''.join(sorted(s, reverse=True))
    return sorted(combined_chars[:34])