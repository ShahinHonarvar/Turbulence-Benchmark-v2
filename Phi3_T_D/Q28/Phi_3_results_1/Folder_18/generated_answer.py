def return_nth_smallest_ascii(input_string):
    substring = input_string[50:60]
    char_values = sorted(set([ord(ch) for ch in substring]))
    if len(char_values) >= 5:
        return chr(char_values[4])
    else:
        return None