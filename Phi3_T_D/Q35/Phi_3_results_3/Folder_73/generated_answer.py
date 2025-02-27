def remove_repeat_chars(s):
    min_char_idx = 10
    max_char_idx = 76 - 1
    char_count = {}
    for i, c in enumerate(s):
        if i < min_char_idx or i > max_char_idx:
            continue
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    cleaned_string = ''.join([c for c in s if c_count[c] == 1 or not char_count.get(c)])
    return cleaned_string