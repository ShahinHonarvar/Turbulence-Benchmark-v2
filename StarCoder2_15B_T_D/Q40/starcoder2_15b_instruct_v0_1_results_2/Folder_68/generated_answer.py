def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted_string[:89]