def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s[:4]]
    sorted_ascii_values = sorted(ascii_values)
    index_of_fourth = min(3, len(sorted_ascii_values) - 1)
    char_of_fourth = chr(sorted_ascii_values[index_of_fourth])
    return char_of_fourth