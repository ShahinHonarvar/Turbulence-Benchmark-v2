def return_nth_smallest_ascii(string):
    chars_in_range = [c for i, c in enumerate(string) if 10 <= i <= 82]
    sorted_chars = sorted(chars_in_range, key=lambda c: ord(c))
    return sorted_chars[17]