def return_n_greatest_chars(input_string: str) -> list:
    sorted_list = sorted(input_string, reverse=True)
    return sorted_list[:19]