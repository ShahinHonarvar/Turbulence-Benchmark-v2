def if_contains_anagrams(strings):
    char_sets = [set(string.lower()) for string in strings]
    freq = {}
    for char_set in char_sets:
        if char_set in freq:
            freq[char_set] += 1
        else:
            freq[char_set] = 1
    counter = 0
    for freq_value in freq.values():
        if freq_value >= 2:
            counter += 1
    return counter >= 6