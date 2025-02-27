def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(1, 47) if 0 <= i < len(s)]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[12] if len(sorted_chars) > 12 else None