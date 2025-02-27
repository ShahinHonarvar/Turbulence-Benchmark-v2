def return_nth_smallest_ascii(s):
    slice = s[14:67]
    sorted_unique_chars = sorted({char for char in slice})
    if len(sorted_unique_chars) < 8:
        return 'Not enough unique characters in the given range.'
    return sorted_unique_chars[7]