def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 1 <= i <= 66 and ord(c) > 0]
    filtered_chars.sort(key=ord)
    return filtered_chars[7]