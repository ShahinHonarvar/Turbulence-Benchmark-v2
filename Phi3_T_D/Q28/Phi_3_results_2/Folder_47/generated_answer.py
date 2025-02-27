def return_nth_smallest_ascii(s):
    filtered_chars = {s[i] for i in range(3, 53) if 3 <= i <= 52}
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None