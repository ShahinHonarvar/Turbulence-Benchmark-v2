def return_n_greatest_chars(string: str) -> str:
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    sorted_chars = [chr(value) for value in sorted_values]
    return ''.join(sorted_chars[:44])