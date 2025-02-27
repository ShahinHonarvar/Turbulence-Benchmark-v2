def remove_repeat_chars(s):
    exclude_range_start, exclude_range_end = (16, 87)
    exclude_range = s[exclude_range_start:exclude_range_end]
    unique_chars = set(exclude_range)
    for char in unique_chars:
        if exclude_range.count(char) > 1:
            s = s[:exclude_range_start] + s[exclude_range_start:exclude_range_end].replace(char, '') + s[exclude_range_end:]
    return s