def return_n_greatest_chars(string_of_chars):
    ascii_values = []
    for char in string_of_chars:
        ascii_values.append(ord(char))
    sorted_ascii_values = sorted(ascii_values)
    return sorted_ascii_values[:14]