def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    return sorted_values[:24]