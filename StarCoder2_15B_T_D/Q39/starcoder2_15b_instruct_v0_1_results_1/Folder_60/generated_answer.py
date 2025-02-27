def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    top_28_values = sorted_values[:28]
    top_28_chars = [chr(value) for value in top_28_values]
    top_28_chars.sort()
    return top_28_chars