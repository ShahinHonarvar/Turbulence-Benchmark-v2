def remove_repeat_chars(input_string: str) -> str:
    unique_chars = set()
    for char in input_string[60:200]:
        unique_chars.add(char)
    repeated_chars = set()
    for char in unique_chars:
        if input_string[60:200].count(char) > 1:
            repeated_chars.add(char)
    output_string = ''
    for char in input_string:
        if char not in repeated_chars:
            output_string += char
    return output_string