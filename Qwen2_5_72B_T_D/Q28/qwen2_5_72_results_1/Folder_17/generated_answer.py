def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(4, 34) if i < len(s)]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[3] if len(sorted_chars) > 3 else None