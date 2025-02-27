def filter_chars(input_string):
    char_to_remove = ''.join((chr(c) for c in range(ord('H') + 1, ord('|'))))
    filtered_chars = [c for c in input_string[18:31] if c not in char_to_remove]
    return input_string[:18] + ''.join(filtered_chars) + input_string[31:]