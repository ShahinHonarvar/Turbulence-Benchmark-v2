def return_nth_smallest_ascii(s):
    substring = s[36:80]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars, key=ord)
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    return None