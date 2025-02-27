def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    anagram_count = {}
    for s in sorted_strings:
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    return sum((count > 1 for count in anagram_count.values())) <= 11