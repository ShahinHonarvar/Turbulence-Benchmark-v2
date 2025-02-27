def return_nth_smallest_ascii(string):
    chars_between_indices = [c for i, c in enumerate(string) if 22 <= i <= 74]
    sorted_chars = sorted(chars_between_indices)
    return sorted_chars[11]