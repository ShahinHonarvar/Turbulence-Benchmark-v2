def return_nth_smallest_ascii(s):
    chars_in_range = [ch for ch in s[21:60] if ch.isalpha()]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[10]