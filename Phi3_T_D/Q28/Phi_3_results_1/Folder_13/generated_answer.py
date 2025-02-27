def return_nth_smallest_ascii(s):
    sub_str = s[47:81]
    sorted_chars = sorted(set(sub_str))
    return sorted_chars[3] if len(sorted_chars) >= 4 else None