def return_nth_smallest_ascii(s):
    filtered_chars = s[5:90]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[12] if len(sorted_chars) > 12 else None