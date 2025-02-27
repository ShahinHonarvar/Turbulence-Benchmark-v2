def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i + 1:], start=i + 1):
            if len(word1) >= 3 and len(word2) >= 3 and (normalize(word1) == normalize(word2)):
                anagram_pairs.add((normalize(word1), i, j))
    return len(anagram_pairs) <= 17