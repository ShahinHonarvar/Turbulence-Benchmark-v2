def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[47:71]]
    filtered_chars.sort(key=ord)
    return filtered_chars[13]