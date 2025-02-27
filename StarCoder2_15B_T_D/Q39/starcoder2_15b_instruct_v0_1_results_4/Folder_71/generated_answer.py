def return_n_greatest_chars(string):
    char_values = {char: ord(char) for char in string}
    sorted_chars = sorted(char_values, key=char_values.get, reverse=True)
    return sorted_chars[:14]