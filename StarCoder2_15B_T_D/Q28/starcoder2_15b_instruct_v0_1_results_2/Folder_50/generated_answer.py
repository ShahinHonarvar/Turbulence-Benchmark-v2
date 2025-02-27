def return_nth_smallest_ascii(string):
    filtered_chars = [c for i, c in enumerate(string) if 25 <= i <= 88]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[10]