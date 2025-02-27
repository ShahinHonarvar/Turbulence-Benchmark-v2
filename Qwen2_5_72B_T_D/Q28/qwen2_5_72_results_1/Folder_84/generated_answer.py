def return_nth_smallest_ascii(s):
    relevant_chars = [s[i] for i in range(52, 80) if i < len(s)]
    relevant_chars.sort(key=ord)
    return relevant_chars[6] if len(relevant_chars) > 6 else None