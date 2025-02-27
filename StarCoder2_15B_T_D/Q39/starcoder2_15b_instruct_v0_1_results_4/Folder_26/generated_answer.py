def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=lambda c: ord(c), reverse=True)
    selected_chars = sorted_string[:43]
    sorted_chars = sorted(selected_chars)
    return sorted_chars