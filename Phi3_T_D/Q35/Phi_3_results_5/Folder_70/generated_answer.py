def remove_repeat_chars(s):
    shaded_part = s[43:71]
    chars_to_remove = {c for c in shaded_part if shaded_part.count(c) > 1}
    for char in chars_to_remove:
        shaded_part = shaded_part.replace(char, '')
    return s[:43] + shaded_part + s[71:]