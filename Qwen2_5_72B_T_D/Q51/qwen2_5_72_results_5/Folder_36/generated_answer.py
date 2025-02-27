def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i + 1:], start=i + 1):
            if len(word1) >= 3 and len(word2) >= 3 and (normalize(word1) == normalize(word2)):
                anagram_pairs.add((min(word1, word2), max(word1, word2)))
    return len(anagram_pairs) <= 25