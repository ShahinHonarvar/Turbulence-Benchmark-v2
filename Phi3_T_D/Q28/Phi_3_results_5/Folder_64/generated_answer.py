def return_nth_smallest_ascii(char_str):
    first_seven_chars = char_str[:7]
    return sorted(first_seven_chars, key=ord)[6]