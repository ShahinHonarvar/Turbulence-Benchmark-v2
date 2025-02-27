def return_nth_smallest_ascii(string: str) -> str:
    substring = string[5:83]
    ascii_values = [ord(c) for c in substring]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii_value = sorted_ascii_values[15]
    for c in string:
        if ord(c) == nth_smallest_ascii_value:
            return c