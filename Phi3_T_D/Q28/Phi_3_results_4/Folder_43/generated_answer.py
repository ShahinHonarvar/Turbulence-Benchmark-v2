def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 14 <= i <= 35]
    filtered_chars.sort(key=ord)
    return filtered_chars[10]