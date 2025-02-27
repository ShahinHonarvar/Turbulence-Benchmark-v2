def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    top_11_values = sorted_values[:11]
    top_11_chars = [chr(value) for value in top_11_values]
    return top_11_chars