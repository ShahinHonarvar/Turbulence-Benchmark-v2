def return_nth_smallest_ascii(input_string):
    relevant_chars = input_string[10:91]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[19]