def return_nth_smallest_ascii(s):
    chars = s[12:73]
    char_freq = {}
    for char in chars:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1])
    return sorted_chars[12][0]