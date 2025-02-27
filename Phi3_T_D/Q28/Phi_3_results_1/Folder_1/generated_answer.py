def return_nth_smallest_ascii(s):
    start, end = (21, min(59, len(s)))
    target_chars = s[start:end + 1]
    target_vals = sorted([ord(ch) for ch in target_chars])
    return chr(target_vals[10]) if len(target_vals) > 10 else None