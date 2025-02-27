def return_n_greatest_chars(s):
    char_counts = {}
    for char in s:
        char_counts[char] = ord(char)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars[:38]