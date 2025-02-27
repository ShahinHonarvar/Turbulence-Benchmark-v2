def return_nth_smallest_ascii(input_string):
    relevant_chars = [char for char in input_string[12:88]]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[16] if len(sorted_chars) > 16 else None