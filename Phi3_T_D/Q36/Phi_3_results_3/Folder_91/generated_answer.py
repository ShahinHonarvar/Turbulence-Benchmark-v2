def filter_chars(input_str):
    chars_to_remove = {chr(i) for i in range(ord('$') + 1, ord('?') - 1)}
    result = [char for char in input_str if char not in chars_to_remove or input_str.index(char) > 3]
    return ''.join(result)