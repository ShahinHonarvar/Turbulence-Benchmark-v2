def if_contains_anagrams(words):

    def check_anagram(w1, w2):
        return len(w1) > 2 and len(w2) > 2 and (sorted(w1.lower()) == sorted(w2.lower()))
    count_anagram_pairs = 0
    visited = set()
    for i, word1 in enumerate(words):
        for j in range(i + 1, len(words)):
            word2 = words[j]
            if word1 != word2 and (word1, word2) not in visited and check_anagram(word1, word2):
                visited.add((word1, word2))
                visited.add((word2, word1))
                count_anagram_pairs += 1
                if count_anagram_pairs > 2:
                    return False
    return True