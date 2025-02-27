def return_nth_smallest_ascii(input_string):
    selected_chars = input_string[24:72]
    char_ascii_list = sorted([ord(char) for char in selected_chars])
    if len(char_ascii_list) < 8:
        return None
    return chr(char_ascii_list[7])