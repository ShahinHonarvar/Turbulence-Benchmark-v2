def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=ord, reverse=True)
    return list(sorted_string[:36])