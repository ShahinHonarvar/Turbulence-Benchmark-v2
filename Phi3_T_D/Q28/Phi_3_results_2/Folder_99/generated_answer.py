def return_nth_smallest_ascii(s):
    unique_chars = {c for i, c in enumerate(s, start=17) if 17 <= i <= 65 and c not in s[:i]}
    return sorted(unique_chars, key=ord)[7] if len(unique_chars) >= 8 else None