from collections import defaultdict

def if_contains_anagrams(strings):
    length_filtered = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    sorted_strings = sorted(length_filtered)
    count = 0
    i = 0
    j = 1
    while j < len(sorted_strings):
        if sorted_strings[i] == sorted_strings[j]:
            count += 1
            j += 2
        elif sorted_strings[i] < sorted_strings[j]:
            j += 1
        i += 1
        if i >= j:
            i = j
            j += 1
    return count >= 44