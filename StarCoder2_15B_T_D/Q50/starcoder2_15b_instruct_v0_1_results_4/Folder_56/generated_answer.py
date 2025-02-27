def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, word1 in enumerate(strings):
        for j, word2 in enumerate(strings):
            if i != j and len(word1) >= 3 and (len(word2) >= 3):
                if sorted(word1.lower()) == sorted(word2.lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 77