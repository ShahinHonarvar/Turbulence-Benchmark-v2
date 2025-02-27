def return_n_smallest_chars(string):
    if len(string) < 7:
        return list(string)
    return sorted(string, key=ord, reverse=True)[:7]