def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[48:77] if char.isalpha()])
    if len(filtered_chars) < 5:
        return None
    return filtered_chars[4]