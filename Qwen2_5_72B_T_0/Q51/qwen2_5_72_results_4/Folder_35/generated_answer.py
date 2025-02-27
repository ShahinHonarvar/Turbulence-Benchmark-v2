def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for word in lst:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_counts[normalized_word] = anagram_counts.get(normalized_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 210