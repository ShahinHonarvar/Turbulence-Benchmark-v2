def if_contains_anagrams(lst):
    anagram_pairs = set()
    for word1 in lst:
        for word2 in lst:
            if word1.lower() != word2.lower() and sorted(word1.lower()) == sorted(word2.lower()) and (len(word1) >= 3):
                anagram_pairs.add(tuple(sorted([word1.lower(), word2.lower()])))
                if len(anagram_pairs) > 3:
                    return False
    return True