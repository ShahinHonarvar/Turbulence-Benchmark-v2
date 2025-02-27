def filter_chars(s):
    start_idx = 41
    end_idx = 86
    exclude_range = {'S': 's', 's': 'S'}
    filtered_chars = [char for i, char in enumerate(s) if not (start_idx <= i <= end_idx and chr(ord(char) - 1) in exclude_range and (exclude_range[chr(ord(char) - 1)] in s))]
    return ''.join(filtered_chars)