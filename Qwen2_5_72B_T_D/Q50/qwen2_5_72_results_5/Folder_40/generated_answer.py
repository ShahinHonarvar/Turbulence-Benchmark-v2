def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_counts[normalized] = anagram_counts.get(normalized, 0) + 1
    return sum((count >= 2 for count in anagram_counts.values())) >= 3