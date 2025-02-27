def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = {}
    for sorted_word in sorted_strings:
        anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1
    return sum((count >= 2 for count in anagram_counts.values())) // 2 <= 30