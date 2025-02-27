def filter_chars(input_str):
    target_char = input_str[73:75]
    filtered_str = ''.join([ch for ch in input_str if not (ch >= target_char[0] and ch <= target_char[1])])
    return filtered_str