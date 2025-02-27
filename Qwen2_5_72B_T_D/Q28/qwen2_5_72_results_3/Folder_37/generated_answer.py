def return_nth_smallest_ascii(s):
    subset = s[28:68]
    subset_chars = [char for char in subset]
    subset_chars.sort(key=lambda x: ord(x))
    if len(subset_chars) < 15:
        return None
    return subset_chars[14]