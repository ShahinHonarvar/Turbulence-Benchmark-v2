def return_n_greatest_chars(string):
    sorted_characters = sorted(string, reverse=True)
    return sorted_characters[:29]