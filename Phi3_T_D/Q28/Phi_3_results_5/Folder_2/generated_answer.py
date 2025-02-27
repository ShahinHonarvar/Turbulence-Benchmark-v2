def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[48:77] if char not in s[:48] + s[77:]]
    return sorted(filtered_chars, key=ord)[4] if len(filtered_chars) >= 5 else None