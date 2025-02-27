def remove_repeat_chars(input_str):
    seq = input_str[13:75]
    to_remove = {char for char in seq if seq.count(char) > 1}
    return ''.join([char for char in input_str if not (char in to_remove and 13 <= input_str.index(char) < 76)])