def return_nth_smallest_ascii(s):
    target_indices = range(15)
    target_chars = [s[i] for i in target_indices]
    return min(target_chars, key=lambda c: ord(c))