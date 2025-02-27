def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return [sorted_chars[i] for i in range(len(sorted_chars) - 1, len(sorted_chars) - 45 - 1, -1)]