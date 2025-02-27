def return_nth_smallest_ascii(s):
    middle_part = s[8:66] if len(s) > 65 else s[8:]
    sorted_chars = sorted(middle_part, key=ord)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    else:
        return None