def return_n_smallest_chars(string):
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    smallest_chars = sorted(char_freq, key=lambda x: ord(x), reverse=True)[:46]
    return smallest_chars