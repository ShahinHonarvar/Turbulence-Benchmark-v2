def if_contains_anagrams(strings):
    filtered_strings = [s for s in strings if s.isalpha() and len(s) >= 3]
    sorted_strings = [''.join(sorted(s.lower())) for s in filtered_strings]
    pairs = [(s1, s2) for i, s1 in enumerate(sorted_strings) for s2 in sorted_strings[i + 1:] if s1 == s2]
    return len(pairs) <= 279