def return_nth_smallest_ascii(s):
    mid_slice = s[8:66]
    sorted_unique_chars = sorted(set(mid_slice), key=lambda char: ord(char))
    if len(sorted_unique_chars) >= 6:
        return sorted_unique_chars[5]
    return None