def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 51 <= i <= 89]
    sorted_chars = sorted(filtered_chars, key=lambda c: ord(c))
    return sorted_chars[13]