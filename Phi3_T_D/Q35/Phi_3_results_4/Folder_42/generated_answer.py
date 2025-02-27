def remove_repeat_chars(s):
    char_counts = {}
    new_string = list(s)
    for i, char in enumerate(s[18:60]):
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            new_string = [c for c in new_string if c != char]
    return ''.join(new_string)