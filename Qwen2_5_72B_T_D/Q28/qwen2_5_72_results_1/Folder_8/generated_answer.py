def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s[60:89] if s.count(c) == 1]
    relevant_chars.sort(key=ord)
    return relevant_chars[6]