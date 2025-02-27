def if_contains_anagrams(strings):
    filtered_strings = [s for s in strings if s.isalpha() and len(s) >= 3]
    sorted_strings = [''.join(sorted(s.lower())) for s in filtered_strings]
    anagram_counts = {}
    for s in sorted_strings:
        if s in anagram_counts:
            anagram_counts[s] += 1
        else:
            anagram_counts[s] = 1
    return max(anagram_counts.values()) <= 289