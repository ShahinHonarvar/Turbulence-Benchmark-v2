def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[48:77] if char in s]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[4] if len(sorted_chars) > 4 else None