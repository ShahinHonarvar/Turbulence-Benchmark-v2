def return_n_smallest_chars(string):
    return sorted(string, key=lambda c: ord(c), reverse=True)[:7]