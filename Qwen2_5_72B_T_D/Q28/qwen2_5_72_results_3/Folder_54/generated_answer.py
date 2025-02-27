def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[12:88] if 32 <= ord(c) <= 126]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[16] if len(sorted_chars) > 16 else None