def return_n_greatest_chars(string):
    if len(string) > 45:
        string = string[:45]
    sorted_string = sorted(string, reverse=True)
    return sorted_string if len(sorted_string) == 45 else sorted_string + [''] * (45 - len(sorted_string))