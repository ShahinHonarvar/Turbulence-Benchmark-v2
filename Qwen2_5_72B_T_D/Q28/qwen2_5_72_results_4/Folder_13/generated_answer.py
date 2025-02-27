def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 47 <= i <= 80]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[3]