def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[47:81]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[3]