from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    length_filtered = defaultdict(list)
    for string in strings:
        clean_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            length_filtered[clean_str].append(string)
    for key in length_filtered:
        if len(length_filtered[key]) > 1:
            anagrams_count += len(length_filtered[key]) * (len(length_filtered[key]) - 1) // 2
    return anagrams_count >= 77