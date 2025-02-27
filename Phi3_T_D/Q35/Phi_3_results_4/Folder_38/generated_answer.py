def remove_repeat_chars(input_string):
    seen_chars = set()
    output_chars = []
    for i, char in enumerate(input_string[36:84]):
        if char not in seen_chars:
            seen_chars.add(char)
            output_chars.append(char)
    return input_string[:36] + ''.join(output_chars) + input_string[84:]