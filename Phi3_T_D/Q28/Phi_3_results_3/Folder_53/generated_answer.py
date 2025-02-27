def return_nth_smallest_ascii(s):
    target_indices = set(range(40, 61))
    eligible_chars = [s[i] for i in target_indices if i < len(s)]
    if len(eligible_chars) < 19:
        return None
    return sorted(eligible_chars)[18]