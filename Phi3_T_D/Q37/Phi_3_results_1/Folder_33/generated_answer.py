def filter_chars(input_string):
    start_idx, end_idx = (722, 832)
    result = [char for char in input_string if not start_idx <= input_string.index(char) <= end_idx or not 'K' <= char <= 'm']
    return ''.join(result)