def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(60, 84) if i < len(s)]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[13] if len(sorted_chars) > 13 else None