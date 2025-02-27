def filter_chars(input_string):
    start_idx = 114
    end_idx = 639
    upper_limit = 'x'
    lower_limit = '!'
    allowed_chars = set((chr(i) for i in range(ord(lower_limit), ord(upper_limit) + 1)))
    altered_string = ''.join((char for idx, char in enumerate(input_string) if idx < start_idx or idx > end_idx or char not in allowed_chars))
    return altered_string