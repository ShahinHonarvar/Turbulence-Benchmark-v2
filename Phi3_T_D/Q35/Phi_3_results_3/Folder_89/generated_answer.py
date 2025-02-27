def remove_repeat_chars(s):
    seq = s[55:83]
    char_counts = {}
    for char in seq:
        char_counts[char] = char_counts.get(char, 0) + 1
    filtered_seq = ''.join((char for char in seq if char_counts[char] > 1))
    return s.replace(filtered_seq, '')