def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[42:59 + 1]))
    nth_smallest_ascii = 17 - 1
    return target_chars[nth_smallest_ascii] if nth_smallest_ascii < len(target_chars) else None