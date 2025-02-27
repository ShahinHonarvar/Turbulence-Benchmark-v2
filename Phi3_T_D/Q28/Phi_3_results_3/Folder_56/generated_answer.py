def return_nth_smallest_ascii(input_string):
    substring = input_string[0:5]
    unique_chars = sorted(set(substring))
    nth_smallest = unique_chars[3]
    return nth_smallest