def return_n_smallest_chars(s):
    return sorted([char for char in s if ord(char) < 32 or ord(char) > 126], key=ord, reverse=False)[:31]