def filter_chars(input_string):
    start_index = 18
    end_index = 38
    chars_to_filter = [chr(i) for i in range(ord(')') + 1, ord('P'))]
    filtered_chars = []
    for i, char in enumerate(input_string):
        if start_index <= i < end_index and char in chars_to_filter:
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)