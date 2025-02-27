def return_n_greatest_chars(string):
    ascii_values = [ord(c) for c in string]
    sorted_values = sorted(ascii_values, reverse=True)
    top_24_values = sorted_values[:24]
    top_24_chars = [chr(value) for value in top_24_values]
    top_24_chars.sort(reverse=True)
    return top_24_chars