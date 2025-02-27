def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    top_32_values = sorted_values[:32]
    top_32_chars = [chr(value) for value in top_32_values]
    return top_32_chars