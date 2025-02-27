def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    top_36_values = sorted_values[:36]
    top_36_chars = [chr(value) for value in top_36_values]
    return top_36_chars