def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda char: ord(char), reverse=True)
    return sorted_chars[:26]