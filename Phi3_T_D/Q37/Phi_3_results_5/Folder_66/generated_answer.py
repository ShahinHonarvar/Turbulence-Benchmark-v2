def filter_chars(input_string):
    filtered_string = [c for i, c in enumerate(input_string) if not (27 <= i <= 85 and ord('c') <= ord(c) <= ord('i'))]
    return ''.join(filtered_string)