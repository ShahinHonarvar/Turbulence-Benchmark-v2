def return_nth_smallest_ascii(s):
    substr = s[20:60]
    characters = set(substr)
    sorted_chars_by_ascii = sorted(characters, key=ord)
    return sorted_chars_by_ascii[10] if len(sorted_chars_by_ascii) > 10 else None