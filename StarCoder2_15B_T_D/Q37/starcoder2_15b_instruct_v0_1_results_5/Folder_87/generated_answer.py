def filter_chars(input_str):
    chars_to_remove = set((chr(c) for c in range(ord('W'), ord('[') + 1)))
    output_str = ''
    for char in input_str:
        if char not in chars_to_remove or input_str.index(char) < 18 or input_str.index(char) > 81:
            output_str += char
    return output_str