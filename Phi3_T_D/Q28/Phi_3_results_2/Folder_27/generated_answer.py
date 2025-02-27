def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[33:86] if char not in '!3456789:;<=>?@AOQRI']
    filtered_chars.sort(key=ord)
    return filtered_chars[12]