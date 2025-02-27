def return_nth_smallest_ascii(s):
    substring = s[25:46]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    if len(unique_chars) < 11:
        return None
    return unique_chars[10]