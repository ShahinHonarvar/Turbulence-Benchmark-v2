def if_contains_anagrams(strings):
    lowercase_strings = [s.lower() for s in strings]
    sorted_strings = [''.join(sorted(s)) for s in lowercase_strings]
    indices_by_sorted_string = {}
    for i, sorted_string in enumerate(sorted_strings):
        indices_by_sorted_string.setdefault(sorted_string, []).append(i)
    num_anagrams = sum((len(indices) > 1 for indices in indices_by_sorted_string.values()))
    return num_anagrams >= 30