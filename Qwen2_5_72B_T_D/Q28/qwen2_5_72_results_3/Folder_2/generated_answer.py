def return_nth_smallest_ascii(s):
    filtered_chars = [ch for ch in s[48:77] if s.count(ch) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[4] if len(sorted_chars) > 4 else None