from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst[i + 1:], start=i + 1):
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1.lower()) == Counter(word2.lower())):
                anagram_pairs.add(tuple(sorted((word1.lower(), word2.lower()))))
    return len(anagram_pairs) <= 210